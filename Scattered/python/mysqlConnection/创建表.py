import pymysql
# 打开建立数据库连接 主机地址 端口号3306 用户名 密码 数据库名
db = pymysql.Connect(host='localhost', port=3306, user='jeffrey', password='hzf13622352971cx', db='spider', charset='utf8')
# 创建一个游标对象 cursor()
cursor = db.cursor()
# 自定义sql语句
sql = """create table tel(
    name varchar(20),
    phone int
)"""
cursor.execute(sql)  # 执行sql语句
db.close()  # 关闭数据库连接

