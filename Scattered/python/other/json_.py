'''
1、JSON(JavaScript Object Notation)特点：
    (1) JSON 是一种轻量级数据交换格式，易于人阅读和编写，
    (2) JSON 具有通用性，支持几乎所有语言，
    (3) JSON 支持跨平台，支持 windows，linux，mac 平台。

2、常用json函数
    json.dumps 将python对象编码成json格式
    json.lodas 将已编码的json字符串编码为python对象

    json.dump 将 json 字符串数据写进文件
    json.load 读取json文件里面的数据

    python    {''python': 1, 'java': 2, 'Hadoop': 3}
              {''python': 1, 'java': 2, 'Hadoop': 3}

    JSON      '{"python": 1, "java": 2, "Hadoop": 3}'

3、python 与 json 类型转换

    python          json

    dict            object
    list,tuple      array
    str             string
    int,float       number
    True            true
    False           false
    None            null


'''
import json
# 简单来讲，json就是js中的对象 数据结构 {key:value,key:value... ...}
# 本质上讲，json就是有固定结构的字符串

# json转字典
j = '{"city": "北京", "name": "熊喵"}'

p = json.loads(j)
print(type(p))

#  字典转json
_dict = {"city": "北京", "name": "熊喵"}

s = json.dumps(_dict, ensure_ascii=False)
print(type(s))