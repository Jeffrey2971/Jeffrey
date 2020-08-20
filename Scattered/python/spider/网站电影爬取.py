import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

reponse = requests.get(url, headers=headers).text

pattern_1 = re.compile(r'{"rating":\["(.*?)","\d+"\]').findall(reponse)
pattern_2 = re.compile(r'"title":"(.*?)"').findall(reponse)

for i in range(len(pattern_1)):
    print('排名：' + str(i+1) + ' 电影名：' + pattern_2[i] + '评分：' + pattern_1[i])
