# 本例演示锁和一些其他线程工具的使用
# _*_ coding:utf-8 _*_
from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaing = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name
    lock.acquire()  # 加锁
    remaing.add(myname)
    print('[%s] started %s' % (ctime(), myname))
    lock.release()  # 释放锁
    sleep(nsec)
    lock.acquire()
    remaing.remove(myname)
    print('[%s] completed %s (%d secs)' % (ctime(), myname, nsec))
    print('(remaining: %s)' % (remaing or 'NONE'))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('all done at:', ctime())

if __name__ == '__main__':
    _main()