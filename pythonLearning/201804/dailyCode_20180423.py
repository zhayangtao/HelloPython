"""
内建模块
"""
import hmac
import itertools

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

# 内建模块 itertools 提供用于操作迭代对象的函数

natuals = itertools.count(1)
# for n in natuals:
#     print(n)

cycle = itertools.cycle('ABC')
# for c in cycle:
#     print(c)

ns = itertools.repeat('A', 3)  # 限定循环次数
for n in ns:
    print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# 任何实现了上下文管理的对象，都能使用 with 语句
# 实现上下文管理是通过 __enter__ 和 __exit__ 两个方法实现的


class Query:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()


# @contextmanager：用于简化编写上下文管理器
from contextlib import contextmanager


class Query:
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q  # 用于把变量输出出去
    print('End')


# @contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去，
# 然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()

# 用 @contextmanager 实现自动执行代码


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('<%s>' % name)


with tag('hi'):
    print('hello')
    print('world')


# 使用 @closing 将没有实现上下文的对象转换为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)
