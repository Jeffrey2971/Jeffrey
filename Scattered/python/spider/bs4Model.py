# BeautifulSoup模块简介和安装
import re
from bs4 import BeautifulSoup

# CSS 选择器：BeautifulSoup4
# 和lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器
# 主要的功能也是如何解析和提取 HTML/XML 数据。


# 模块下载安装：pip install bs4

# 基础例子
html = """
<html><head><title>The Dormouse's story</title><title>The Dormouse's story2</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 解析字符串形式的html

soup = BeautifulSoup(html, 'lxml')
'''
print(soup.prettify())  # prettify() 方法可让代码更加可视化(格式化代码)

print(soup.title())  # 根据标签名获取标签信息

print(soup.title.string)  # 根据标签名获取标签信息内的信息

print(soup.title.name)  # 获取标标签名

print(soup.p.attrs['name'])  # 获取标签内所有属性

print(soup.head.contents)  # 直接获取子标签

for i in soup.head.children:  # 获取子标签但结果为生成器
    print(i)

for i in soup.p.descendants:  # 获取所有子标签,结果为生成器
    print(i)

# 搜索文档树 findall() 方法

data_1 = soup.find_all('a')  # 查找所有的a标签，返回一个结果集，内容为标签对象
print(type(data_1[0]))
for i in data_1:
    print(i)

data_2 = soup.find_all(re.compile("^b"))  # 根据正则表达式查找标签
for i in data_2:
    print(i)

data_3 = soup.find_all(id="link2")  # 根据属性查找标签
for i in data_3:
    print(i)

# 根据标签内容获取标签内容
data_4 = soup.find_all(text="Lacie")
print(data_4)

data_5 = soup.find_all(text=["Lacie", "Tillie"])
print(data_5)

data_6 = soup.find_all(text=re.compile("Do"))  # 可用正则表达式查找
print(data_6)

# 总结：实际编程中更多使用的方法为data_1或data_3
'''

# CSS 选择器 (根据CSS样式表来查找标签，对应方法为select() )
# CSS 选择器类型：标签选择器，类选择器，ID选择器

data_7 = soup.select('a')  # 通过标签名获取标签
print(type(data_7))  # 与data_3不同的是，data_3输出结果为一个结果集而data_7输出为一个列表

data_8 = soup.select(".sister")  # 通过类名查找
print(data_8)

data_9 = soup.select("#link2")  # 通过ID查找
print(data_9)

data_10 = soup.select("p #link1") # 组合查找(p标签下的#link1)
print(data_10)

data_11 = soup.select('a[href="http://example.com/elsie"]')  # 通过其他属性查找
print(data_11)