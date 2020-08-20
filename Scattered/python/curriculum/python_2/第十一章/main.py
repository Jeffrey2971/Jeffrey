# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/1/18 15:26
# @Author  : lemon



# f = open('/Users/lemonlxn/Desktop/test/files/文本.txt',mode='r',encoding='utf-8')
#
# data = f.read()
# print(data)
#
# f.close()


# with open('files/文本.txt',mode='r',encoding='utf-8') as f:
#     data = f.readlines()
#     print(data[0])


with open('files/文本_new.txt',mode='a',encoding='utf-8') as f:
    f.write('hello lemon\n hello world\n')
    f.writelines(['hello pycharm\n','hello apple\n','hello'])