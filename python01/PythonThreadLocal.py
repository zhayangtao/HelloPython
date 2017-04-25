import threading

# 全局 ThreadLocal对象
local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Blice',), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()


# 分布式进程
# 通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
# 先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
import random, time, queue
from multiprocessing.managers import BaseManager
# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()

# 从 BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue注册到网络上