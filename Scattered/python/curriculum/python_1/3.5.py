import req模块get请求

response=req模块get请求.get("http://www.baidu.com")

#1.获取返回的cookiejar对象
cookiejar=response.cookies

#2.将cookiejar转换成字典
cookiedict=req模块get请求.utils.dict_from_cookiejar(cookiejar)

print(cookiejar)