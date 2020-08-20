'''

正文

　　读取文件的三个方法：read()、readline()、readlines()。均可接受一个变量用以限制每次读取的数据量，但通常不使用。本章目的是分析和总结三种读取方式的使用方法和特点。

回到顶部
一、read方法
　　特点是：读取整个文件，将文件内容放到一个字符串变量中。

　　劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。

复制代码
file = open('兼职模特联系方式.txt', 'r')  # 创建的这个文件，也是一个可迭代对象

try:
    text = file.read()  # 结果为str类型
    print(type(text))
    print(text)
finally:
    file.close()
"""
<class 'str'>
吴迪 177 70 13888888
王思 170 50 13988888
白雪 167 48 13324434
黄蓉 166 46 13828382
"""
复制代码
　　read()直接读取字节到字符串中，包括了换行符

>>> file = open('兼职模特联系方式.txt', 'r')
>>> a = file.read()
>>> a
'吴迪 177 70 13888888\n王思 170 50 13988888\n白雪 167 48 13324434\n黄蓉 166 46 13828382'
回到顶部
二、readline方法
　　特点：readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存

　　缺点：比readlines慢得多

复制代码
file = open('兼职模特联系方式.txt', 'r')

try:
    while True:
        text_line = file.readline()
        if text_line:
            print(type(text_line), text_line)
        else:
            break
finally:
    file.close()
"""
<class 'str'> 吴迪 177 70 13888888

<class 'str'> 王思 170 50 13988888

<class 'str'> 白雪 167 48 13324434

<class 'str'> 黄蓉 166 46 13828382
"""
复制代码
　　readline()  读取整行，包括行结束符，并作为字符串返回

>>> file = open('兼职模特联系方式.txt', 'r')
>>> a = file.readline()
>>> a
'吴迪 177 70 13888888\n'

三、readlines方法
　　特点：一次性读取整个文件；自动将文件内容分析成一个行的列表。

复制代码
file = open('兼职模特联系方式.txt', 'r')

try:
    text_lines = file.readlines()
    print(type(text_lines), text_lines)
    for line in text_lines:
        print(type(line), line)
finally:
    file.close()
"""
<class 'list'> ['吴迪 177 70 13888888\n', '王思 170 50 13988888\n', '白雪 167 48 13324434\n', '黄蓉 166 46 13828382']
<class 'str'> 吴迪 177 70 13888888

<class 'str'> 王思 170 50 13988888

<class 'str'> 白雪 167 48 13324434

<class 'str'> 黄蓉 166 46 13828382
"""
复制代码
　　readlines()读取所有行然后把它们作为一个字符串列表返回。

>>> file = open('兼职模特联系方式.txt', 'r')
>>> a = file.readlines()
>>> a

['吴迪 177 70 13888888\n', '王思 170 50 13988888\n', '白雪 167 48 13324434\n', '黄蓉 166 46 13828382']

'''