import os

# print('process (%s) start' % os.getpid())
# pid = os.fork()  # linux/unix 系统使用
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid()), os.getppid())
# else:
#     print('I (%s) just created a child proceee (%s).' % (os.getpid(), pid))

from multiprocessing import Process


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')

# 线程池
from multiprocessing import Pool
import time, random


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(('Task %s runs %0.2f seconds.' % (name, (end - start))))


if __name__ == '__main__':
    print('Parent process %s ' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    """
    对Pool对象调用join()方法会等待所有子进程执行完毕，
    调用join()之前必须先调用close()，
    调用close()之后就不能继续添加新的Process了 
    """
    p.close()
    p.join()
    print('All subprocesses done')

# 子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 进程间通信
# 以Queue为例，创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(('Process to read: %s' % os.getpid()))
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程，写入
    pw.start()
    # 启动子进程，读取
    pr.start()
    # 等待pw结束
    pw.join()
    # 强制终止 pr
    pr.terminate()


# 多线程
"""
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
threading是高级模块，对_thread进行了封装。绝大多数情况下，
我们只需要使用threading这个高级模块。
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行。
"""
import time, threading
def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s ended' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)



