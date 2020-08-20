'''
不能调用下方的函数

test()

def test():
    print('hello')
    return
'''

'''
正确写法

def test():
    print('hello')
    return

test()
'''


def add(x, y):
    result = x + y
    return result
add(5, 6)


