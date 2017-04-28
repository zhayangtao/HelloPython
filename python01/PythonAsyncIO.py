import asyncio


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


# async/await
async def hello():
    print('Hello world')
    r = await asyncio.sleep(1)
    print('Hello again')


# 获取 Eventloop
loop = asyncio.get_event_loop()
# 执行
loop.run_until_complete(hello())
loop.close()
