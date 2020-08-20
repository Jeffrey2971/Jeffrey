# 自定义一个迭代器
# 以类为例：
# 需要在类中实现两个方法 __iter__ 与 __next__

# 其中：
# 1、__iter__ 方法需要返回对象本身，它是for循环使用中迭代器的要求，
# 2、__next__ 方法用于返回容器中的下一个元素，当容器中的数据取完时，需要引发 stopiteration 异常

# 需求：
# 1、自定义迭代器，通过传入最小值最大值，返回该范围所有数值的三次方
# 2、将返回的值，存入num_list列表中

'''
import time

test_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test_iter = iter(test_list)
next(test_iter)

while True:
    print(next(test_iter))
    time.sleep(1)

'''


class Number():
    def __init__(self,min,max):
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        # 返回这个范围内所有数值的三次方
        num = self.min

        if self.min <= self.max:
            self.min += 1
            return num ** 3
        else:
            raise StopIteration


_list = []
for i in Number(2, 8):
    _list.append(i)

print(_list)










