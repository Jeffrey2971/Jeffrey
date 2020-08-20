
# 如果搜索的是数字或者英文，比如：java  经删减后返回以下网址
# https://www.baidu.com/s?wd=python  wd后等于搜索的关键字

# 如果搜索的是中文或其他字符，比如：北京  经删减后返回以下网址
# https://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC wd后等于搜索的关键字 北京

from urllib import request
import urllib.parse

url = 'https://www.baidu.com/s?'

# 构造url编码
wdd = urllib.parse.urlencode({'wd': '北京'})

url = url + wdd

req = request.Request(url)

reponse = request.urlopen(req).read().decode()

print(reponse)
