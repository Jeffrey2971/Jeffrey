import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) '
                  'AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56'
                  ' Safari/535.11'
}

# 创建session对象
ses = requests.session()

# 构造登陆所需参数
data = {'email': '13169523261', 'password': 'hzf13622352971cx'}

# 通过传递用户登录名密码参数得到cookie信息
ses.post('http://renren.com/PLoding.do', data=data, headers=headers)

# 需要请求的页面
reponse = ses.get('http://www.renren.com/880151247/profile')

print(reponse.content.decode())
