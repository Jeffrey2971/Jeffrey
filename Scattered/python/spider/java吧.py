# http://tieba.baidu.com/f?kw=java&fr=ala0&pn=0 第一页 (1-1)*50
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=50 第二页 (2-1)*50
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=100 第三页 (3-1)*50
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=150 第四页 (4-1)*50
# http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=200 第五页 (5-1)*50
# http://tieba.baidu.com/f?kw=java&pn=100
from urllib import request
import urllib.parse

path = r'/Users/jeffrey/test'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}


def loadPage(urlmax, filename):
    print('正在下载：' + filename)
    req = request.Request(urlmax, headers=header)
    response = request.urlopen(req).read
    return response


def writepage(html, filename):
    print('正在保存：' + filename)
    with open(filename, mode='wb') as f:
        f.write(html)
    print('------------------------')


def tiebaSpider(beginPage, endPage, url):  # 构造url
    for page in range(beginPage, endPage + 1):  # page 循环传入参数beginPage, endPage, url
        pn = (page - 1) * 50  # 计算pn值
        urlmax = url + '&pn=' + str(pn)  # 完整的url
        print(urlmax)
        filename = 'd:\\第' + str(beginPage) + '页.html'

        html = loadPage(urlmax, filename)  # 调用爬虫
        writepage(html, filename)  # 把获取到的信息写入到本地


if __name__ == '__main__':
    kw = (input('要爬取的贴吧名：'))
    beginPage = int(input('请输入爬取起始页：'))
    endPage = int(input('请输入爬取结束页：'))

    url_min = 'http://tieba.baidu.com/f?'

    key = urllib.parse.urlencode({'kw': kw})  # 防止用户输入中文

    url = url_min + key

    tiebaSpider(beginPage, endPage, url)
