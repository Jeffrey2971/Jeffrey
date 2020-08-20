from urllib import request
import random
proxylist = [
    {'http': '113.195.171.212:9999'},
    {'http': '223.198.16.26:9999'},
    {'http': '117.69.201.13:9999'},
    {'http': '117.57.90.102:9999'},
    {'http': '123.54.45.32:9999'},
    {'http': '114.239.2.161:9999'}
]

proxy = random.choice(proxylist)

# 构建代理处理对象
proxyhandler = request.ProxyHandler(proxy)

# 创建自定义opener
opener = request.build_opener(proxyhandler)

# 创建请求对象
req = request.Request('http://www.baidu.com/')

# 发送请求
res = opener.open(req).read().decode()

print(res)

