import pymysql

db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='stu', charset='utf8')
cursor = db.cursor()
sql = 'update student set age=age+1'
cursor.execute(sql)
db.commit()
db.close()
