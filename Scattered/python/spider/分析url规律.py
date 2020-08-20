from urllib import request
import urllib
import time

#构造请求头信息
header = {
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}

# 分析 url 规律
# http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5 第一页 pn=0 （1-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 第二页 （2-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 第三页 （3-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 第四页 （4-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=200 第五页 （5-1）*50

for i in range(1, 3):
    print('http://tieba.baidu.com/f?kw=python&fr=ala0&pn=' + str((i-1)*50))  # str后面必须带()

























