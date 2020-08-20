from urllib import request

url = r'https://careers.tencent.com/search.html?index=1'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

reponse = request.Request(url, headers=header)
data = request.urlopen(reponse)
print(data.read().decode())
