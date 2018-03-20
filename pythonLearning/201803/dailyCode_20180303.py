def gensquares(N):
    for i in range(N):
        yield i ** 2


for i in gensquares(5):
    print(i, end=' : ')


gen = gensquares(5)
next(gen)
gen.send(5)


def gensquares2():
    for i in range(10):
        yield i ** 2


for i in gensquares2():
    print(i, end=' : ')


gen = gensquares2()
next(gen)
print(gen.send(5))

G = (x ** 2 for x in range(4))
next(G)
print('*****************')
print(G.send(77))
sorted((x ** 2 for x in range(4)), reverse=True)


# 自定义 map 函数
def mymap(func, *seqs):
    res = []
    for agrs in zip(*seqs):
        res.append(func(*agrs))
    return res


print(list(zip([1, 2, 3], [2, 3, 4, 5])))


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    print('seqs=', seqs)
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


S2, S1 = 'abc', 'zyz123'
print(myzip(S1, S2))


def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


print(mymapPad(S1, S2))


# 生成器模式
def mymapYidle(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def mymapPadYield(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


print(list(mymapYidle(S1, S2)))
print(list(mymapPadYield(S1, S2)))


def test():
    return (1)


def myzipBetter(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iter]
        yield tuple(res)


print([x + y for x in 'ab' for y in 'dnd'])


import time


reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)