import requests
from bs4 import BeautifulSoup

url = r'https://www.mzitu.com/page/2/'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


html = requests.get(url, headers=header).text

soup = BeautifulSoup(html, 'lxml')

url_1 = soup.find("ul", {"id":"pins"}).find_all("img")


# print(soup.prettify())

print(url_1)




# //*[@id="pins"]/li[6]/a/img
# //*[@id="pins"]/li[1]/a/img