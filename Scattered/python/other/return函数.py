
#程序运行到第一个return时，一般情况下会跳出改函数块不再执行下面的代码
#try excepy finally
def test():
    a=1
    return a
    print('我不会被执行')
test()
