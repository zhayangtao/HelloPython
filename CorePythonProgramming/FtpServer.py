from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# 实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()
# 添加用户权限，括号内的参数是(用户名， 密码， 用户目录， 权限)
"""
e	改变文件目录
l	列出文件
r	从服务器接收文件
写权限 ：

a	文件上传
d	删除文件
f	文件重命名
m	创建文件
w	写权限
M	文件传输模式（通过FTP设置文件权限 ）
"""
authorizer.add_user('user', '1234', 'f://', perm='elradm')
# 添加匿名用户，只需要路径
authorizer.add_anonymous('f://')
# 初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer

# 添加被动端口范围
handler.passive_ports = range(21, 24)
# 监听ip和端口
server = FTPServer(('192.168.1.203', 21), handler)
# 开始服务
server.serve_forever()