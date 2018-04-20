"""
Lock
"""


import threading

balance = 0


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# 使用 lock 确保线程同步
balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 请求获得锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁


print('_' * 30)
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


"""
ThreadLocal
"""

import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


"""
分布式进程
"""


import random
import queue
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


# 把两个 Queue 注册到网络上， callable 参数关联 Queue 对象"""  """
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口 5000，设置验证码 'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动 Queue
manager.start()
# 获取通过网络访问的 Queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放置任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从 result 队列读取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result %s' % r)

manager.shutdown()
print('master exit.')
