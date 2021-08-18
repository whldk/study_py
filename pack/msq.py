#!/usr/bin/python3

import mysql.connector as mysql

db = mysql.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="mengoo_common"
)


mycursor = db.cursor()

mycursor.execute("select * from admin")

result = mycursor.fetchall()

for x in result:
    print(x)