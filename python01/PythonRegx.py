# 正则表达式
s = 'ABC\\-001'
s = r'ABC\-001'

import re

re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

# 分组 用()表示的就是要提取的分组（Group）。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  # 原始字符串
print(m.group(1))
print(m.group(2))

# 预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())

x = 1 + 2 + \
    3 + 4

list(map((lambda x: x ** 2), range(10)))
list(filter((lambda x: x % 2 == 0), range(5)))

list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10))))
res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)


def gensquares(N):
    for i in range(N):
        yield i ** 2


for i in gensquares(5):
    print(i, end=' : ')


def gen():
    for i in range(10):
        x = yield i
        print(x)


g = gen()
next(g)

[x ** 2 for x in range(5)]  # list
g = (x ** 2 for x in range(5))  # generator
list(x ** 2 for x in range(5))

for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2.0))

''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))

list(map(abs, (-1, -1, 3, 4)))
list(abs(x) for x in (-1, -2, 3, 4))
list(map(lambda x: x * 2, (1, 2, 3, 4)))
list(x * 2 for x in (1, 2, 3, 4))

import math

list(map(math.sqrt, (x ** 2 for x in range(4))))

print(next(g))


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


list(both(5))

import os

for (root, subs, files) in os.walk('.'):
    for name in files:
        if name.startswith('call'):
            print(root, name)


def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res


print(scramble('spam'))

print('********************')


def scramble(seq):
    for i in range(len(seq)):
        yield from seq[i:] + seq[:i]


g = scramble('spam')
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('list', list(scramble('spam')))
print('********************')


def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


g = scramble('spam')
print('list', list(scramble('spam')))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('list', list(scramble('spam')))


def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute1(rest):
                res.append(seq[i:i + 1] + x)
        return res


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]
            for x in permute2(rest):
                yield seq[i:i + 1] + x


print(list(scramble('abc')))
print(permute1('abc'))


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


import time


def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start


s = 'spam'
for (offset, item) in enumerate(s):
    print(item, 'appears at offset', offset)

os.system('systeminfo')


def f(a, b, c, d):
    print(a, b, c, d, sep='&')


x = 'old'
y = "x"


def changer():
    global x
    x = 'new'


def outer():
    nonlocal y
    x = 'old'

    def changer():
        nonlocal x
        x = 'new'
        y = 2


def squares(x):
    for i in range(x):
        yield i ** 2


funcs = [lambda x: x ** 2, lambda x: x ** 3]

if x:
    def func():
        pass
else:
    def func():
        pass

L = {1, 2, 3}


def test():
    nonlocal L
    L = x


x = 99


def setX(new):
    global x
    x = new


def maker(M):
    return lambda x: x ** M

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i **x)
    return acts
