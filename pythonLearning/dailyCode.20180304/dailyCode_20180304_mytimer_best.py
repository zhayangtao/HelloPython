"""
use 3+ keyword-only default arguments, instead of ** and dict pops
"""
import time
import sys


trace = lambda *args: None
timefunc = time.clock if sys.platform == 'win32' else time.time


def timer(func, *args, _reps=1000, **kargs):
    trace(func, args, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*args, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)


def best(func, *args, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *args, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)
