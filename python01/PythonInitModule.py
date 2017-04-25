# python 内建模块
# **********  datetime
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
# 指定日期
dt = datetime(2017, 4, 25)
print(dt)

# datetime 转换为 timestamp
print(dt.timestamp())
# timestamp 转换为 datetime
t = 1493049600.0
print(datetime.fromtimestamp(t))
# str 转换为 datetime
cday = datetime.strptime('2017-04-25 00:00:00', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime 转换为 str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


# datetime 加减
from datetime import datetime, timedelta
now = datetime.now()
now + timedelta(hours=10)
now - timedelta(days=1)
now + timedelta(hours=10, days=1)


# **********   collections
# 1.namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x
p.y

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# 2.deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import  deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 2.defaultdict
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1


# hashlib  摘要算法
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


# xml
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self, name):
        print('sax:end_element: %s' % name)
    def char_data(self, text):
        print('sax:char_data: %s' % text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# HTMLParser
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

# urllib
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
