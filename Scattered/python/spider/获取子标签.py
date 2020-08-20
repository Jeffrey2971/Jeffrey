from lxml import etree
html = etree.parse(r'C:\Users\Jeffr\PycharmProjects\test-pc\爬虫\html\hello.html')

result = html.xpath('//li/a')  # 单斜杠标识获取下一级子标签
result_2 = html.xpath('//li//span')  # 双斜杠表示获取所有符合条件的子标签
result_3 = html.xpath('//li/a//@class')  # 获取li标签下a标签内所有的class
print(result_3)