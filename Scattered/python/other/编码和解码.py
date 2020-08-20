# encode() decode()
# python3 中字符串的两种类型：1、bytes（存储二进制类型）2、str（存储unicode类型）
# 编码格式和解码格式要一致
# 字符串(unicode)转byte (编码)

a = '北京天安门'
b = a.encode('utf-8')  # 转成字节码
print(b)

# byte转字符串 (解码)
c = b.decode('utf-8')  # (解码)
print(c)