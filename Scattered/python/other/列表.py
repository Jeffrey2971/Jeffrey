my_num = 1, 3, 5, 6, 9

friends = ['Jeffrey', 'Mable', 'Tom', 'Karen', 'Jeffrey', 'mable']
          #   0          1       2       3   ->索引顺序默认从左至右从0开始
          #  -4         -3      -2      -1
print(friends)  # 打印完整列表

print(friends[0])  # 打印列表内第四个元素

print(friends[-3])  # 打印倒数第三个元素

print(friends[1:])  # 表示打印第二个元素和后面的所有元素

print(friends[1:3])  # 表示打印第二个和第三个元素但不包括第四个元素

friends[1] = 'jm'  # 修改第二个元素为jm

# append()函数
l1 = [1, 2, 3, 4, 5, ]
l1.append([6, 7, 8, 9, ])
# l1.append(*[6, 7, 8, 9, ]) #会报错
print(l1)
l1.extend([6, 7, 8, 9])
print(l1)

# extend()函数

l1 = [1, 2, 3, 4, 5, ]
l1.extend([6, 7, 8, 9])
print(l1)
l1.extend('abc')
print(l1)
l1.extend('a') # 也是可迭代对象
print(l1)
# l1.extend(1) # 报错，不可迭代
print(l1)

# 输出
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'a']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'a']
'''

friends.insert(2, 'None')  # .insert()函数可在指定为的后面添加元素

friends.remove('None')  # .remove()函数可在移除指定为的元素

#friends.clear()  # .clear()方法可重置列表

friends.pop()  # .pop()函数默认移除最后一个元素，可在()内输入需倒数移除的元素

print(friends.index('Jeffrey'))  # 使用.index()获取元素在第几元素

print(friends.count('Mable'))  # .count()函数可计算有几个元素

print(friends.sort())  # .sort()函数可对元素进行a-z0-9顺序排序

print(friends.reverse())  # .reverse()函数可对元素进行颠倒操作

friends2 = friends.copy()  # .copy()函数可继承对象







print(friends)