# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/12 10:48
# @Author  : lemon



# ZeroDivisionError,ValueError


# def f(num):
#     try:
#         return int(num)
#     except (ZeroDivisionError,ValueError) as e:
#         print(e)
#
#     finally:
#         print('执行结束')
#
#
# def f1(num):
#     try:
#         return int(num)
#     except Exception as e:
#         print(e)
#     finally:
#         print('执行结束')





# 需求1：
# 1.传入一个参数，判断是否为整形类型，如果不是，则抛出异常，终止程序。
# 2.判断是否大于等于5，如果小于5，则抛出异常，终止程序。

def f2(num):
    # if not isinstance(num,int):
    #     raise Exception('该参数不是一个整形类型')
    # if num < 5:
    #     raise Exception('该参数小于5')

    assert isinstance(num,int),'该参数不是一个整形类型'
    assert num >=5,'该参数小于5'






# 需求2：

# 传入若干个参数，判断参数个数如果小于等于5，则抛出异常，终止程序

def f3(*args):
    # if len(args)<=5:
    #     raise Exception('该参数个数小于等于5')

    assert len(args)>5,'该参数个数小于等于5'


if __name__ == '__main__':
    f3(1,2,3,4,5,6)

