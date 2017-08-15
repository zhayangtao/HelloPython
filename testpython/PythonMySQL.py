import pymysql
#创建连接
conn = pymysql.connect(host='192.168.1.203', port=3306, user='root', passwd='1234', db='zytdb')
#创建游标
cursor = conn.cursor()
conn.set_charset('utf-8')

cursor.execute('SET CHARACTER SET utf8')

