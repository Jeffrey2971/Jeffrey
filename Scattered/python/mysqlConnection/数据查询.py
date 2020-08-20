import pymysql
db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='stu', charset='utf8')
cursor = db.cursor()

# sql = "select * from student where id=1" data_1
sql = "select * from student"  # data_2

cursor.execute(sql)

# data_1 = cursor.fetchone()  # 获取单个对象 （一行数据）
data_2 = cursor.fetchall()  # 获取多个数据 （多行数据）

print(data_2)
