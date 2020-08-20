# append的用法
'''
_list = []
for i in range(1, 10):
    _list.append(i)  # 需要注意的是每次只能指定一个值

print(_list)
'''

A = [1, 2, 3]
B = 4
C = A.append(B)
# 若B是数字或字符串，直接加到列表末尾
print(A)  # 结果 [1, 2, 3, 4] 会直接修改原列表
print(C)  # 结果 None 无返回值

B = [4]
C = A.append(B)
# 若B是列表，直接将列表添加到末尾，不论有几个列表值
print(A)  # 结果 [1, 2, 3, 4, [4]]
print(C)  # 结果 None

B = [4, 5]
C = A.append(B)
print(A)  # 结果 [1, 2, 3, 4, [4], [4, 5]]
print(C)  # 结果 None
