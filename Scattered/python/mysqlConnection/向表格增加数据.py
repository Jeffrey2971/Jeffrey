import pymysql

db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='stu', charset='utf8')
cursor = db.cursor()
sql = '''insert into student (id,name,age)
    values (2,'李四',14)
'''

cursor.execute(sql)
db.commit()
db.close()