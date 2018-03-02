from dailyCode_20180301 import counters
from dailyCode_20180301 import inc
from functools import reduce
import operator


list(map((lambda x: x + 3), counters))

counters.append(2)
print(counters)


def mymap(func, seq):
    '''
    mymap document
    '''
    res = []
    for x in seq:
        res.append(func(x))
    return res


mymap(inc, [1, 2, 3])


print(list(range(-5, 6)))
print(list(filter(lambda x: x > 0, range(-5, 5))))


# reduce 函数
reduce((lambda x, y: x + y), [1, 2, 3, 4])


def myreduce(func, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = func(tally, next)
    return tally


print(operator.eq(1, 3))


def boo(x):
    return 4 > x > 2


# 使用 filter
print(list(filter(boo, [1, 2, 3, 4])))

[x for x in range(5) if x % 2 == 0]
list(filter(lambda x: x % 2 == 0, range(5)))
list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
[(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]


res = []
for row in range(2):
    pass


####################################################
# 生成器
####################################################
def gensquares(N):
    for i in range(N):
        yield i ** 2


x = gensquares(4)
print(next((x)))
print(next((x)))
print(next((x)))
print(next((x)))


def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
        return res


# 扩展生成器函数协议：send 和 next
def gen():
    for i in range(10):
        x = yield i
        print(x)


G = gen()
print(next(G))
print(next(G))
print(G.send(77))
print(next(G))
print(next(G))


# 生成器表达式
(x ** 2 for x in range(4))
