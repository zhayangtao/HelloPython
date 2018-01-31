#!/usr/bin/env python
# 创建一个TCP客户端，它提示用户输入发送到服务器端的消息，
# 并接收从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户

from socket import *

HOST = '192.168.1.203'
PORT = 21567
BUFSIZ = 1024  # 1KB
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    print(data)
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()
