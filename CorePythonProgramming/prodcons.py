# 该生产者-消费者问题的实现使用了Queue对象，以及随机生产的商品的数量。生产者和消费者独立且并发执行线程
from random import randint
from time import sleep
from queue import Queue
from mtsleepE import MyThread
from atexit import register


def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    val = queue.get()
    print('consumed object from Q... size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def _main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()


@register
def _atexit():
    print('all done')


if __name__ == '__main__':
    _main()
