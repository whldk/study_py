#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="mengoo_common", charset="utf8")

cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
      ('Mac', 'Mohan', 20, 'M', 2000)


try:
    # 执行sql语句
    res = cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()




db.close()