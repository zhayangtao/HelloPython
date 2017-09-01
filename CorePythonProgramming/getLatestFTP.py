#!/usr/bin/env python
# 这个程序用于测试ftp
import ftplib
import os
import socket

HOST = '192.168.1.203'
DIRN = '/'
FILE = 'readme.txt'


def main():
    try:
        f = ftplib.FTP(HOST)  # 连接服务器
    except (socket.error, socket.gaierror) as e:
        print('error: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login()  # 登录
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')

    try:
        print("*** current path: ", f.pwd())
        f.cwd(DIRN)  # 切换目录
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write) # 下载文件
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s" to CWD' % FILE)
        os.unlink(FILE)
    else:
        print('*** Downloaded "%s" to CWD' % FILE)
    f.quit()


if __name__ == '__main__':
    main()
