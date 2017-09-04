#!/usr/bin/env python
# 这个脚本下载并且显示Python新闻组comp.lang.python 中最新一篇文章的前20个“有意义的”行
import nntplib
import socket


HOST = "192.168.1.203"
GRNM = 'comp.lang.python'
USET = 'wesley'
PASS = 'youllNeverGuess'


def main():
    try:
        n = nntplib.NNTP(HOST)
    except socket.gaierror as e:
        print('ERROR: cannot reach host "%s"' % HOST)
        print('("%s")' % eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR: access denied on "%s"' % HOST)
        print('("%s")' % eval(str(e))[1])
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError as ee:
        print('ERROR: cannot load group "%s"' % GRNM)
        print('("%s")' % eval(str(ee))[1])
        print('Server may require authentication')
        print('Uncomment/edit login line above')
        n.quit()
        return
