#!/usr/bin/env python
# 使用SMTP发送邮件，并通过pop从服务器取回邮件
from smtplib import SMTP
from poplib import POP3
from time import sleep


SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop3.163.com'

who = '17600102144@163.com'
toWho = '1264214725@qq.com'
body = '''
From: %(who)s
To: %(toWho)s
Subject: attachment
Hello World!
''' % {'who': who, 'toWho': toWho}

origBody = ['zha1264214725@gmail.com']
origMsg = '\r\n\r\n'.join(['\r\n'.join(body),
                           '\r\n'.join(origBody)])
print(origMsg)
sendSvr = SMTP(SMTPSVR)
sendSvr.login('17600102144@163.com', 'zha1264214725')
errs = sendSvr.sendmail(who, (toWho,), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('17600102144@163.com')
recvSvr.pass_('zha1264214725')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep + 1:]
assert origBody == recvBody