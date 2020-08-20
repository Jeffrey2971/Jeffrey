import datetime

# 获取当前的日期
time = datetime.datetime.now()
print(type(time))

# # 获取指定日期
# time = datetime.datetime(2019, 5, 20, 12, 23, 40)
# print(time)
#
# # 日期转字符串
# time = datetime.datetime.now()
# now = time.strftime('%Y-%m-%d %H:%M:%S')
# print(now)
#
# # 字符串转日期
# s = '2020-8-15 2:30:20'
# d = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
# print(type(d))
