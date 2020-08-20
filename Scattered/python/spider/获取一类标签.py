from lxml import etree

html = etree.parse(r'C:\Users\Jeffr\PycharmProjects\test-pc\Example\hello.html')
result = html.xpath('//span')  # 获取所有span标签的信息

print(result[0].text)


