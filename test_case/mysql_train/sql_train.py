import pymysql

from public import Config

'''1.创建连接'''

conn = pymysql.connect(**Config.sql_conn_dict)
cur = conn.cursor()

'''数据库操作'''
sql = "select* from user"
#含有参数，多个参数用数组的形式放置参数
#id = 2
#sql = "select * from student where id = %s" %id
#cur.execute(sql)
#多个参数值，id = ('1','2','3')
#多个参数，多个值

#sql = "select * from studen where id = %s"
#cur.execute(sql,id)
#cur.scroll(0,mode='absolute')
#cur.scroll(0,mode = 'relative') 绝对移动和相对移动
#结果都为字典
#print(cur.execute(sql))
#print(cur.fetchone()) #fetchone默认取一个值
#print(cur.fetchmany()) #展示多行
#print(cur.fetchall())#展示取数
'''增删改'''
sql = "update user set username = 'wh' where id = 0"
#sql = "select * from user"
cur.execute(sql)
#增删改需要提交
conn.commit()
'''
sq11 =
sql2=
try:
    cur.excute(sql1)
    cur.excute(sql2)
    conn.commit()
    print('True')
except Exceptioin as e:
    conn.rollback()
'''
'''关闭数据库连接'''
cur.close()
conn.close()
