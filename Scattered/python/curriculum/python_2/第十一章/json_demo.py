# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/11 14:44
# @Author  : lemon

import json


def f1():
    '''
    对python对象进行操作
    '''

    # json.dumps
    # 将 Python 对象编码成 JSON 字符串

    p_list = [
                {'lemon':True,'apple':6},
                {'pear':6,'banana':False}
    ]

    p_dict = {'python':1,'Java':2,'Hadoop':None}

    json_list = json.dumps(p_list)
    json_dict = json.dumps(p_dict)



    # json.loads
    # 将 已编码的 JSON 字符串解码为 Python 对象

    list1 = json.loads(json_list)
    dict1 = json.loads(json_dict)

    pass


def f2():
    '''
    文件的读写
    '''

    # 写入JSON文件
    p_dict = '{"python": 1, "Java": 2, "Hadoop":null,"lemon":true,"banana":false}'

    with open('files/json_test.json','w',encoding='utf-8') as f:
        json.dump(p_dict,f)



    # 读取JSON文件

    with open('files/json_test.json','r',encoding='utf-8') as f:
        data = json.load(f)
        data1 = json.loads(data)
        print(data)
        print(data1)





if __name__ == '__main__':
    f2()

