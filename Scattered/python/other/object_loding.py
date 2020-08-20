import time#时间函数

print("Loading",end = "")
for i in range(6):
    print(".",end = '',flush = True)
    time.sleep(0.5)
    if i==1:
        break
    print('执行完毕')