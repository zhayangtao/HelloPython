#!/usr/bin/env python
# 时间戳TCP客户端
from socket import *

HOST = '192.168.1.203'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(('%s\r\n' % data).encode("UTF-8"))
    data = tcpCliSock.recv(BUFSIZ).decode("UTF-8")
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()

