# requests 第三方模块
"""
import requests
r = requests.get('http://www.douban.com')
print(r.status_code)
print(r.text)
# 带参数的 URL
r = requests.get('https://www.douban.com/search',
                 params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.text)


headers = {'AppId': 'dbd170e5-990a-4ee4-b539-95b0f972286c',
           'AppSecret': 'zoLGVgiEPjb8utSpihnh'}
# 带 header 的 URL
r = requests.get('http://172.16.1.141:8080/ymmopenapi/sgw/v1/content/knowledge/keyword?gCode=middle&kCode=fetalEducation',
                 headers=headers)
print(r.status_code, r.reason)
print(r.text)
print(r.encoding)
print(r.content)

r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params)
"""

# psutil
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())


import socket

# 创建一个 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('baidu.html', 'wb') as f:
    f.write(html)
