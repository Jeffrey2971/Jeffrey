# 例子一： 简单的自定义opener()

import urllib.request

# 第一步：构建一个HTTPHandler 处理器对象，支持处理HTTP请求

http_handler = urllib.request.HTTPHandler()

# 第二步：调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象

opener = urllib.request.build_opener(http_handler)

# 第三步：构建 Request请求

request = urllib.request.Request("http://www.baidu.com/")

# 第四步：调用自定义opener对象的open()方法类似urlopen，发送request请求

response = opener.open(request)

# 第五步：获取服务器响应内容

print(response.read().decode())
