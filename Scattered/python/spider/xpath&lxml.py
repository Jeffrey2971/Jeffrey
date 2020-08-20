# pip install lxml
from Example import *
from lxml import etree
"""
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">张三</a></li>
        <li class="item-1"><a href="link2.html">李四</a></li>
        <li class="item-inactive"><a href="link3.html">王五</a></li>
        <li class="item-1"><a href="link4.html">赵六</a></li>
        <li class="item-0"><a href="link5.html">老七</a></li>
    </ul>
</div>



html = etree.HTML(text)  # etree.HTML()方法将字符串解析成了特殊的html对象

result = etree.tostring(html, encoding='utf-8').decode()  # 将html对象转换为字符串

print(result)
"""

# 解析本地html
# 爬虫中网页处理方式：
# 1、在爬虫中，数据获取和数据清洗一体，HTML()
# 2、数据获取和数据清洗分开，parse()


# 获取本地html文档
html = etree.parse(r'C:\Users\Jeffr\PycharmProjects\test-pc\Example\hello.html')
result = etree.tostring(html, encoding='utf-8').decode()

print(result)
