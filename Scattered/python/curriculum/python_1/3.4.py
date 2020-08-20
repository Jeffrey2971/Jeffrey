import req模块get请求

#设置ip地址
proxy={
"http":"http://101.248.64.72:80",
"http":"http://101.248.64.68:80",
"https":"https://101.248.64.72:80",
}

response=req模块get请求.get("http://www.baidu.com", proxies=proxy)

print(response.content.decode())