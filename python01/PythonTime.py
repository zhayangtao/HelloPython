import time, sys

timer = time.clock() if sys.platform[:3] == 'win' else time.time()


def total(reps, func, *args, **kwargs):
    """total time to run func() reps times"""
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)

