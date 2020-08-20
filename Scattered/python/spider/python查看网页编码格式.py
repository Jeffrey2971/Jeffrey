# 需要用到chardet模块

from urllib import request
import chardet

r = request.urlopen('http://www.baidu.com/')
rr = r.read()
rrr = chardet.detect(rr)
print(rrr)
