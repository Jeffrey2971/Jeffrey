from lxml import etree
import winreg
import requests

url = r'http://www.lovehhy.net/Joke/Detail/QSBK/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,  # 获取系统桌面地址
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
path = (winreg.QueryValueEx(key, "Desktop")[0])
reponse = requests.get(url, headers=header).content.decode('GBK')

html = etree.HTML(reponse)

pattern_title = html.xpath('//div/h3[@class="red"]/a[@target="_blank"]')
pattern_text = html.xpath('//div[@id="endtext"]')
num = 0
for x, y in zip(pattern_title, pattern_text):
    num += 1
    _read = str(num) + '： ' + x.text + '：' + y.text + '\n\n\n'
    print(_read)
    with open(path + '\\1.txt', 'a') as f:
        f.write(_read)
