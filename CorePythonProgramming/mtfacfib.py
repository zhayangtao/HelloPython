# 单线程和多线程执行对比
# 在这个多线程该应用中，将先后使用单线程和多线程的方式分别执行三个独立的递归函数
from mtsleepE import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))


def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x - 1))


funcs = [fib, fac, sum]
n = 12


def mainFunc():
    nfuncs = range(len(funcs))
    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('*** multiple threads')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('add done')


if __name__ == '__main__':
    mainFunc()