import pymysql
import requests
import re


# 建立连接
db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='spider', charset='utf8')
cursor = db.cursor()

# 爬取数据
reponse = requests.get('http://changyongdianhuahaoma.51240.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}).text
data_1 = re.compile(r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>').findall(reponse)
data_2 = re.compile(r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>').findall(reponse)


result_list = []
for i in range(len(data_1)):
    result_list.append(data_1[i] + data_2[i])
    sql = "insert into tel(name,phone) values('" + data_1[i] + "','" + data_2[i] + "')"
    # sql = "insert into tel(name,phone) values('" + data_1[i] + "','" + data_2[i] + "')"
    cursor.execute(sql)
print(result_list)

db.commit()
db.close()