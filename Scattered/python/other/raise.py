try:
    s = None
    if s is None:
        print("s 是空对象")
        raise NameError  # 如果引发NameError异常，后面的代码将不能执行
    print(len(s))  # 这句不会执行，但是后面的except还是会走到
except TypeError:
    print("空对象没有长度")

s = None
if s is None:
    raise NameError
print('is here?')  # 如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里
