import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import os

url = "https://www.mzitu.com"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "Referer": "https://www.mzitu.com/101553"
}
def load_page(url):
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            print('页面请求完毕')
            return res.text
    except:
        print('网络访问错误')
#获取整个页面
def get_page(url):
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'lxml')
    #获取首页所有妹子页面
    all_url = soup.find("ul",{"id":"pins"}).find_all("a")
    # print(all_url)
    count = 1
    for href in all_url:
        count=count+1
        # print(href)
        if count % 2 != 0:
            href1 = href['href']  #查找匹配出分页面中的page链接
            # print(href1)
            for href2 in href:
                res2 = requests.get(href1,headers=headers)
                soup2 = BeautifulSoup(res2.text,'lxml')
                # pict_url = soup2.find("div",{"class":"main-image"}).find("img")['src']  #图片链接
                # print(pict_url)
                next_pic = soup2.find_all("span")[9]
                max_url = next_pic.get_text()
                name = soup2.find("div",{"class":"main-image"}).find("img")['alt']
                os.mkdir(name) #第一张图名称作为目录
                os.chdir(name)
                for i in range(1,int(max_url)+1):
                    next_url = href1+'/'+str(i)
                    res3 = requests.get(next_url,headers=headers)
                    soup3 = BeautifulSoup(res3.text,'lxml')
                    pic_address = soup3.find("div",{"class":"main-image"}).find('img')['src']
                    title = soup3.find('h2')
                    name1 = title.get_text()
                    img = requests.get(pic_address,headers=headers)
                    with open(name1+'.jpg','wb') as f:
                        f.write(img.content)

if __name__ == '__main__':
    load_page(url)
    get_page(url)
