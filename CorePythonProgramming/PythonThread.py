# 使用单线程执行循环
from time import sleep, ctime


def loop():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('starting at:', ctime())
    loop()
    loop1()
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()

