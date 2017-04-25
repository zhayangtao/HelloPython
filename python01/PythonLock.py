import time, threading
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

# 创建一个锁就是通过threading.Lock()来实现：
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()
print(balance)