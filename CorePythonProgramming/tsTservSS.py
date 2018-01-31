#!/usr/bin/env python
# 使用 SocketServer、TCPServer、StreamRequestHandler 创建一个时间戳TCP服务器
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode("UTF-8"))).encode("UTF-8"))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
