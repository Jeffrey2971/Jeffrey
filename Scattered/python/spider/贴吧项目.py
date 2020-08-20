import urllib
import urllib.parse
import urllib.request
import time
import os
# 分析 url 规律
# http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5 第一页 pn=0 （1-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 第二页 （2-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 第三页 （3-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 第四页 （4-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=200 第五页 （5-1）*50

# 根据url发送请求，获取服务器响应文件
def loadPage(url, filename):
    print('正在下载 ' + filename)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)'
                             ' AppleWebKit/535.11 (KHTML, like Gecko)'
                             ' Chrome/17.0.963.56 Safari/535.11'}
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request).read()


# 将html内容写入到本地
def writePage(html, filename):
    print('正在保存 ' + filename)
    # 写入文件
    with open(filename, 'wb') as f:
        f.write(html)
    print('***********************************')

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage, endPage + 1):  # 循环处理
        time.sleep(2)
        pn = (page - 1) * 50
        filename = 'd:/第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        # print(fullurl)
        html = loadPage(fullurl, filename)
        # print(html)
        writePage(html, filename)
        print('完成。')


if __name__ == '__main__':
    kw = (input('请输入需要爬取得贴吧名：'))
    beginPage = int(input('请输入起始页：'))
    endPage = int(input('请输入结束页：'))

    url = 'http://tieba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw': kw})
    fullurl = url+key
    tiebaSpider(fullurl, beginPage, endPage)

print('已完成，按任意键退出。')
os.system('pause>nul')
exit()
