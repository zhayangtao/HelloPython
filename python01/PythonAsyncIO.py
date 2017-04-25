#  协程
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)

import asyncio
@asyncio.coroutine
def hello():
    print('Hello, world')
    # 异步调用
    r = yield from asyncio.sleep(1)
    print('Hello again')
# 获取 Eventloop
loop = asyncio.get_event_loop()
# 执行
loop.run_until_complete(hello())
loop.close()


# async/await
async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    print('Hello agein')
# 获取 Eventloop
loop = asyncio.get_event_loop()
# 执行
loop.run_until_complete(hello())
loop.close()