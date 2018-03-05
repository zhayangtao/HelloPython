import sys
import time

[x + y for x in [1, 2, 3] for y in [4, 5, 6]]
{x + y for x in [1, 2, 3] for y in [4, 5, 6]}
{x: y for x in [1, 2, 3] for y in [4, 5, 6]}


# 对模块计时
reps = 1000
repslist = range(reps)


def timer(func, *args, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*args, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))


def genExpr():
    return list(abs(x) for x in repslist)


def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, elapsed, result[0], result[-1]))
