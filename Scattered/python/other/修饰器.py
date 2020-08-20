def decorate(func):
    def wrapper(*args, **kwargs):
        print('执行开始')
        func()
        print('执行结束')
    return wrapper


@decorate
def func():
    print('hello func')


func()
