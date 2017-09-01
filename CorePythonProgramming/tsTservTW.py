#!/usr/bin/env python
# 交互式FTP示例
from ftplib import FTP


f = FTP('ftp.python.org')
f.login('anonymous', 'guido@python.org')
