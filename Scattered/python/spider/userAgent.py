from urllib import request
import random
import re


url = r'http://www.bathome.net/'

# 谷歌浏览器
agent_1 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# qq浏览器
agent_2 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
# 火狐
agent_3 = 'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
# Safari
agent_4 = 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
# 360
agent_5 = 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)'

agent_list = [agent_1, agent_2, agent_3, agent_4, agent_5]

agent = random.choice(agent_list)

# 构造请求头信息

header = {
'User-Agent':agent
}


# 发送请求

req = request.Request(url, headers=header)  # 自定义请求用对对抗反爬虫 request.Request 其中Request是方法名。
reponse = request.urlopen(req).read().decode('GBK')  # 解码decode()  编码encode()

# with open('C:\\Users\\hongj\\Desktop\\test.txt', 'a') as a: a.write(reponse)

fin = re.findall('<title>(.*?)</title>', reponse)

print(fin[0])





















































