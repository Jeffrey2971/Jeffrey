from urllib import request

url = 'http://www.baidu.com/'

# print(request.urlopen(url).read().decode())  # 使用urllib下的request模块下的urlopen方法打开链接.read()

a = request.Request(url)

print(request.urlopen(a).read().decode())