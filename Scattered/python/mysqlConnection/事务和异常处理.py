import pymysql

db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='stu', charset='utf8')
cursor = db.cursor()
sql_1 = 'delete from student where id=1'
sql_2 = 'delete from student where idd=2'  # 错误的语句
try:
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    db.commit()  # 提交事务 （事务：一个事务就是一个不可分割的整体，事务中的操作要么都执行，要么都不执行，把sql_1和sql_2合并为一个事务)）
except Exception as e:
    db.rollback()  # 回滚 （撤销所有操作，包括正确的语句）
    print('出现异常！' + str(e))
db.close()
