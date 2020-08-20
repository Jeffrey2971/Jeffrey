import requests

# session可永久保存cookie对象

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}

# 创建session对象
ses = requests.session()

# 构造登陆需要的参数
data = {'username': '13169523261', 'password': 'hzf13622352971cx'}

# 通过传递用户名密码得到cookie信息
ses.post('http://www.bathome.net/logging.php?action=login', data=data, headers=headers)

# 需要请求的页面
reponse = ses.get('http://www.bathome.net/thread-54509-1-1.html')
print(reponse.content.decode('GBK'))
