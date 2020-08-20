# from urllib import request
# list = [
#     'http://www.baidu.com/',
#     'http://www.baidu.com/',
#     'http://www.baidu.com/',
#     'http://www.baidu.com/',
#     'http://ASJDKLASJDOKASJK12338190238.com',
#     'http://www.baidu.com/',
#     'http://www.baidu.com/'
# ]
#
# i = 0
#
# for url in list:
#     try:
#         i += 1
#         request.urlopen(url)
#         print('第', i, '次请求')
#     except Exception as error:
#         print('发生错误：',error)


def r1(num):  # ZeroDivisionError异常捕捉
    try:
        num / 0
    except (ZeroDivisionError, ValueError) as error:
        print(error)
    finally:
        print('over')


def r2(num):  # ValueError异常捕捉
    try:
        return int(num)
    except ValueError as error:
        print(error)
    finally:
        print('over')

def r3(num):
    assert isinstance(num, int),'该参数不是一个整形类型'
    assert num >= 5, '该参数小于等于5'

if __name__ == '__main__':

    r3('fark')



"""
1、捕获异常的基本格式
try:
    语句一 # 检测语句一是否存在错误
except 异常名称：
    语句二 # 若语句一存在错误，可捕获错误
finally:
    语句三 # 无论语句是否存在错误，都会执行finally内的代码

2、常见异常名称：
    BaseException   所有异常错误
    Exception   常规异常错误
    ZeroDivisionError   除0异常错误
    ValueError  值类型异常错误
    
    更多异常：http://www.runoob.com/python/python-exceptions.html
    
3、raise 抛出异常
    除了try-except-finally还可使用raise
    可通过raise显示引发的异常
    一旦引发raise后面的异常，将终止程序运行

4、assert 断言
    基本格式：
        assert bool_expression [, arguments]
    
    如果 bool_expression 为 False ,则不会抛出 arguments 这个自定义异常信息
    如果 bool_expression 为 True , 则不会抛出 arguments 这个自定义异常信息
    
"""