

#global函数可以重新设置全局变量

apple = 5


def shuiguo():

    global apple
    apple=10
    print('函数内的apple为：'+str(apple))

shuiguo()
print('apple的全局变量为：'+str(apple))