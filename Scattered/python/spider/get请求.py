# https://www.baidu.com/s?wd=python
# https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC  url 编码
from urllib import request
import urllib
import urllib.parse
wd = {'wd': '北京'}
url = 'https://www.baidu.com/s?'
wdd = urllib.parse.urlencode(wd)
r_url = url + wdd
print(r_url)

