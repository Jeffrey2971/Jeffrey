


A = [1, 2, 3]
B = "try"
C = A.extend(B)
# 若B是字符串，依次添加到列表的末尾
print(A)  # 结果 [1, 2, 3, 't', 'r', 'y'] 会直接修改原列表
print(C)  # 结果 None 无返回值

B = [4, 5]
C = A.extend(B)
# 若B是列表，会打散后添加到末尾，不论有几个列表值
print(A)  # 结果 [1, 2, 3, 't', 'r', 'y', 4, 5]
print(C)  # 结果 None
