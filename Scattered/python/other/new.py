
apple=6

def shuiguo():
    global apple,lemmo#global函数设置函数为全局变量，如未设置就叫做局部变量
    apple=5
    lemmo=10
shuiguo()
print(apple,lemmo,sep=',')