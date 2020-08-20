import requests
# reponse = requests.request('get','http://www.baidu.com/').content.decode()

# print(requests.get('http://www.baidu.com/').content.decode()) 基本请求

# ------------------使用requests添加请求头和参数

header = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}

# https://www.baidu.com/s?wd=java

wd = {'wd': 'java'}
reponse = requests.get('http://www.baidu.com/s?',params=wd,headers=header)

data_1 = reponse.text  # 返回一个字符串形式的数据

data_2 = reponse.content  # 返回一个二进制形式的数据


print(data_2)
