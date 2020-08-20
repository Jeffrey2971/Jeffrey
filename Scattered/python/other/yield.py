def f1():  # yield将方法转换为一个生成器
    list_ = []
    for i in range(1,10):
        list_.append(i)
    return list_




def f2():  # yield将方法转换为一个生成器
    for i in range(1,10):
        yield i

# print(f1())
gen = f2()

for x in gen:
    print(x)
