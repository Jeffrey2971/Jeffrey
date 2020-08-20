import urllib
import urllib.parse
from urllib import request

def tiebaSpider(url, begin, end):
    for i in range(begin, end + 1):
        pn = (i-1)*50
        fullurl = url_ + '&pn=' + str((i-1)*50)
        filename = 'c:/第' + str(pn) + '页'

if __name__ == '__main__':
    kw = (input('请输入贴吧名：'))
    begin = int(input('请输入起始页：'))
    end = int(input('请输入结束页：'))

    url = 'http: // tieba.baidu.com/f?'
    key = urllib.parse.urlencode({'kw': kw})
    print(key)
    url_ = url+key
