import threading
import asyncio
import random

"""
@asyncio.coroutine
def hello():
    print('Hello world')
    # 异步调用
    r = yield from asyncio.sleep(1)
    print('Hello again')


# 获取 Eventloop
loop = asyncio.get_event_loop()
# 执行
loop.run_until_complete(hello())
loop.close()


@asyncio.coroutine
def hello():
    print('Hello world (%s)' % threading.currentThread)
    yield from asyncio.sleep(1)
    print('Hello again (%s)' % threading.currentThread)


# 获取 Eventloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
"""


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        yield from asyncio.sleep(random.random())
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
