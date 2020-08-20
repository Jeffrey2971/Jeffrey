from lxml import etree
html = etree.parse(r'C:\Users\Jeffr\PycharmProjects\test-pc\爬虫\html\hello.html')
# result = html.xpath('//li[@class="item-88"]')
result = html.xpath('//li/a[@href="link2.html"]')
print(result[0].text)