import asyncio

@asyncio.coroutine
def hello():
    print("hello world")
    r = yield from asyncio.sleep(1)
    print("hello again")


# 新语法
async def hello():
    print("hello world")
    r = await asyncio.sleep(1)
    print("hello again")

