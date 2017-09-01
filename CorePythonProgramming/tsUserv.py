#!/usr/bin/env python
# 创建一个UDP服务器，接收客户端发来的消息
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    data = data.decode()
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
    print('received from and returned to:', addr)
udpSerSock.close()