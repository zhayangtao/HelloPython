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
(x ** 2 for x in range(5))  # generator
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
