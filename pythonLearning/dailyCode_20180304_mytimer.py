"""
timer(spam, 1, 2, a = 3)
"""
import time
import sys
from dailyCode_20180304 import forLoop, listComp, mapCall, genExpr, genFunc

if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time


def trace(*args): pass


def timer(func, *args, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, *args, kargs, _reps)
    repslist = range(_reps)
    start = timefunc()
    for i in repslist:
        ret = func(*args, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)


def best(func, *aargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *kargs, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)


print(sys.version)
for tester in (timer, best):
    print('<%s>' % tester.__name__)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = tester(test)
        print('-' * 33)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, elapsed, result[0], result[-1]))
