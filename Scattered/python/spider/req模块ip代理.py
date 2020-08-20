import requests

# 设置ip地址
proxy = {
    'http': 'http://59.52.187.119:9999',
}

reponse = requests.get('http://www.mzitu.com/page/1/', proxies=proxy)

print(reponse.content.decode())
