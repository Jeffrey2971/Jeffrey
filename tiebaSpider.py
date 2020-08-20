import urllib
import urllib.request
import urllib.parse
import time
import os
from lxml import etree

class Spider(object):
    def __init__(self):
        self.tiebaName = '王者荣耀'
        self.beginPage = 1
        self.endPage = 5
        self.header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.min_url = 'http://tieba.baidu.com/f?'
        self.min_url_link = 'http://tieba.baidu.com'
        self.Path = r'C:\Users\Jeffrey\Desktop\img\\'
        self.fileName = 1
        global fileName, Path, tiebaName
    def tiebaSpider(self):  # 构造每页的url链接
        for size in range(self.beginPage, self.endPage+1):
            try:
                pn = (size-1)*50
                _key = {'kw': self.tiebaName}
                key = urllib.parse.urlencode(_key)
                # print(self.min_url + str(key) + '&pn=' + str(pn))
                max_url = self.min_url + str(key) + '&pn=' + str(pn)
                # print(max_url)
                self.loadPage(max_url)
            except Exception as error:
                print('构造url页码时出现了错误，原因为：' + str(error))

    def loadPage(self, url):  # 构造每页内容并提取出每页的帖子
        try:
            reponse = urllib.request.Request(url, headers=self.header)
            data_url_html = urllib.request.urlopen(reponse).read()

            '''
        <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6370235547" title="出FILCO花纹红，87键双模，花尽买的，不到半个月，需要的" target="_blank" class="j_th_tit ">出FILCO花纹红，87键双模，花尽买的，不到半个月，需要的</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author " title="主题作者: 0花花花花大人0" data-field="{&quot;user_id&quot;:1294178963}"><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer" data-field="{&quot;un&quot;:&quot;0\u82b1\u82b1\u82b1\u82b1\u5927\u4eba0&quot;,&quot;id&quot;:&quot;tb.1.cf8601c2.OsMDhQ65nHwNIMDGizr-ig&quot;}" class="frs-author-name j_user_card " href="/home/main/?un=0%E8%8A%B1%E8%8A%B1%E8%8A%B1%E8%8A%B1%E5%A4%A7%E4%BA%BA0&amp;ie=utf-8&amp;id=tb.1.cf8601c2.OsMDhQ65nHwNIMDGizr-ig&amp;fr=frs" target="_blank">0花花花...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">12-2</span>
</div>
            </div>
        '''

            html_url = etree.HTML(data_url_html)
            html_url_pattern = html_url.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
            # print(html_url_pattern)
            for link in html_url_pattern:
                links = self.min_url_link + link
                #print(links)
                self.loadImage(links)
        except Exception as error:
            print('提取每页下的帖子时出现了错误，原因为：' + str(error))

    def loadImage(self, links):   # 构造并提取每篇帖子下的jpg图片地址
        try:
            reponse_url_image = urllib.request.Request(links, headers=self.header)
            data_url_image = urllib.request.urlopen(reponse_url_image).read()
            # print(data_url_image)
            html_url_image = etree.HTML(data_url_image)
            # print(html_url_image)
            '''
            <cc><div class="j_ueg_post_content p_forbidden_tip" style="display:none;">该楼层疑似违规已被系统折叠&nbsp;<a rel="noopener" href="###" class="p_forbidden_post_content_unfold" style="display:;">隐藏此楼</a><a rel="noopener" href="###" class="p_forbidden_post_content_fold" style="display:none;">查看此楼</a></div><div id="post_content_128636008016" class="d_post_content j_d_post_content  clearfix" style="display:;">            那个大佬帮忙看下是不是真的，谢谢<br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=abf8f289b9fd5266a72b3c1c9b189799/130bc958ccbf6c81aa39d28ab33eb13532fa40cb.jpg" size="83926" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=e634fea8e9cd7b89e96c3a8b3f244291/bc739a8ba61ea8d3cf2c8a66980a304e241f58cb.jpg" size="123954" changedsize="true" width="560" height="746" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=9792f1d5e650352ab16125006342fb1a/059a7b2762d0f7033cee6bbe07fa513d2797c5fa.jpg" size="83926" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=4cc3495055afa40f3cc6ced59b64038c/f0b77f09c93d70cf04f4546ff7dcd100bba12bcb.jpg" size="81113" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=72d61bf003f431adbcd243317b37ac0f/1fdb8022720e0cf317abb0990546f21fbf09aafa.jpg" size="79939" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=4cc7fea88d8ba61edfeec827713597cc/b688393fb80e7beca915fb83202eb9389a506b0b.jpg" size="61508" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=858781bf21738bd4c421b239918b876c/ddefc8160924ab18c8181f553afae6cd7a890bcb.jpg" size="57533" changedsize="true" width="560" height="418" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=6bcee58faccc7cd9fa2d34d109002104/7d96a6096b63f624ac01c7618844ebf81b4ca3fa.jpg" size="99394" changedsize="true" width="560" height="746" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><br><div class="replace_div" style="width: 560px;"><img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=eb62334b8918367aad897fd51e738b68/de5399cb39dbb6fd09551b440624ab18962b37cb.jpg" size="164433" changedsize="true" width="560" height="1210" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;"><div class="replace_tip" style="width: 558px;"><em class="expand"></em><span class="txt">点击展开，查看完整图片</span></div></div></div><br>            </cc>
            '''
            html_url_image_pattern = html_url_image.xpath('//img[@class="BDE_Image"]/@src')
            # print(html_url_image_pattern)
            for url_image in html_url_image_pattern:
                self.writeImage(url_image)
        except Exception as error:
            print('构造并提取每篇帖子下的jpg图片地址时出现了错误，原因为：' + str(error))

    def writeImage(self, links_image):
        try:
            print('正在保存第 ' + str(self.fileName) + '... ...')
            image = urllib.request.urlopen(links_image).read()
            file = open(self.Path + str(self.fileName) + '.jpg', 'wb')
            file.write(image)
            file.close()
            self.fileName += 1
            time.sleep(2)
        except Exception as error:
            print('二进制数据写入本地图片时发生了错误，原因为：' + str(error))


if __name__ == '__main__':  # 接口对象实例化
    mySpider = Spider()
    mySpider.tiebaSpider()

os.system('pause>nul')
quit()
# finish at 12/23/1.25

