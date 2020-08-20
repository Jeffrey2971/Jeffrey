q, w = 0, 0
v = input("请输入内容>>>")
for item in v:
    if item > "0" and item < "9":
        q += 1
    if (item > "a" and item < "z") or (item > "A" and item < "Z"):
        w += 1
print("一共输入%s个数字和%s字母" % (q, w))

