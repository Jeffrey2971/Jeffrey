import xlsxwriter

import requests
import re

reponse = requests.get('http://changyongdianhuahaoma.51240.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}).text
data_1 = re.compile(r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>').findall(reponse)
data_2 = re.compile(r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>').findall(reponse)

result_list = []
workbook = xlsxwriter.Workbook('demo2.xlsx')
worksheet = workbook.add_worksheet()

for i in range(len(data_1)):
    result_list.append(data_1[i] + data_2[i])
    worksheet.write('A' + str(i+1), data_1[i])
    worksheet.write('B' + str(i+1), data_2[i])

workbook.close()
