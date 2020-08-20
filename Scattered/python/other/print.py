print('jeffrey')#打印jeffrey 字符串需要用逗号隔开

print('jeffrey', 'mable')#打印jeffrey和mable，打印多个字符需要用逗号隔开

print('jeffrey', 'mable', sep=',')#打印jeffrey和Mable并用逗号隔开，用到函数sep

print('jeffrey', 'mable', sep=',', end='.')# 打印jeffrey和mable用逗号隔开并在结尾添加.，用到函数end和sep

import time

print("---RUNOOB EXAMPLE ： Loading 效果---")

print("Loading",end = "")
for i in range(20):
    print(".", end='', flush=True)
    time.sleep(0.5)