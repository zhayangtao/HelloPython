from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


# multiple alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('hello world\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body>Hello world</body></html>')
    email.attach(html)
    return email

# multipart: images
def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    return email

def sendMsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    print('Sending multipart atlernative msg...')
    msg = make_mpa_msg()
    