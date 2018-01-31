#!/usr/bin/env python
# 创建一个TCP服务器，接收来自客户端的消息，然后将消息加上时间戳前缀并发送回客户端

from socket import *
from time import ctime

HOST = ''  # HOST 变量是空白的，这是对 bind()方法的标识，表示它可以使用任何可用的地址。
PORT = 21567
BUFSIZ = 1024  # 1kb
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 网络间TCP通信
tcpSerSock.bind(ADDR)  # 绑定地址
tcpSerSock.listen(5)  # 监听5个客户端

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ).decode()  # 一次性接收指定大小的数据
        print(data)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
        tcpCliSock.send('hello world')

    tcpCliSock.close()
tcpSerSock.close()
