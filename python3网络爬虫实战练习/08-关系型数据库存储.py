#连接数据库
import pymysql

# db=pymysql.connect(host='localhost',user='root',password='748491',port=3306)
# cursor=db.cursor()
# cursor.execute('select version()')
# data=cursor.fetchone()
# print('database version:',data)
# cursor.execute('create database spiders default character set utf8')
# db.close()

#创建表
id='101'
user='job'
age='22'
db=pymysql.connect(host='localhost',user='root',password='748491',port=3306,db='spiders')
#sql='create table if not exists students (id varchar(255) not null,name varchar(255) not null,age int not null ,primary key(id))'
#注意传入数据的时候尽量使用这种格式化符的形式，有几个value写几个%s,只需要在execute()方法的第一个参数传入该sql语句，value值统一传一个元组就好了
sql='insert into students(id,name,age) values(%s,%s,%s)'
cursor=db.cursor()
# cursor.execute(sql1)
try:
    cursor.execute(sql,(id,user,age))
    db.commit()          #必须执行commit()方法才能将数据插入数据库中
except:
    db.rollback()        #异常处理，如果插入数据失败，就执行一次回滚，相当于什么都没有发生过
db.close()
