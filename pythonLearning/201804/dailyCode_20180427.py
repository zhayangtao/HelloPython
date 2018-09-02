"""
异步 IO
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)


"""
asyncio
"""


import asyncio
import threading


@asyncio.coroutine
def hello():
    print('Hello World!')
    r = yield from asyncio.sleep(1)
    print('Hello again!')


loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
# loop.close()


@asyncio.coroutine
def hello():
    print('Hello world!(%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again!(%s)' % threading.currentThread())


print('_' * 30)
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s hreader > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


print('_' * 30)
loop = asyncio.get_event_loop()
tasks = [wget(host)
         for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


"""
async/wait：用于替换 asyncio
"""


async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    print('Hello agein!')


"""
aiohttp
"""

from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
