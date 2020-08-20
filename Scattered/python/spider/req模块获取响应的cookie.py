import requests

reponse = requests.get('http://www.baidu.com/')


cookiejar = requests.utils.dict_from_cookiejar(reponse.cookies)

print(cookiejar)