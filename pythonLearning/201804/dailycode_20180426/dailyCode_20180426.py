"""
访问数据库
"""

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='1234', db='sampledb', charset='utf8')
# 创建游标
cursor = conn.cursor()
# 执行 sql
effect_row = cursor.execute('select * from user')
print(effect_row)
cursor.close()
conn.close()


import requests
headers = {'AppId': 'dbd170e5-990a-4ee4-b539-95b0f972286c',
           'AppSecret': 'zoLGVgiEPjb8utSpihnh'}
# 带 header 的 URL
r = requests.get('http://172.16.1.140/ymmopenapi/sgw/v1/content/knowledge/detail/407281256',
                 headers=headers)
print(r.status_code, r.reason)
print(r.text)
print(r.encoding)
print(r.content)


def application(environ, start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


from wsgiref.simple_server import make_server
# httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000')
# httpd.serve_forever()
