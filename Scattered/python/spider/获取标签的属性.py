from lxml import etree
import requests
html = etree.parse(r'C:\Users\Jeffr\PycharmProjects\test-pc\爬虫\html\hello.html')
#result = html.xpath('//li/@class')
result = html.xpath('//li/a/@href')
for i in result:
    requests.get(i)
