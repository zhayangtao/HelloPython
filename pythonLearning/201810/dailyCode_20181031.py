import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print('waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {} s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    dones, pendings = await asyncio.wait(tasks)

    for task in tasks:
        print('Task ret: ', task.result())

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print('Time: ', now() - start)

# 列表内涵
leaps = [y for y in range(1900, 1940) if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]

s = {7, 'veil', 0, ("x", 11)}

set_ = set('apple')
set_2 = set('aple')
print(set_ == set_2)

# 集合内涵
html = {x for x in range(1, 2, 3)}
# 固定集合
frozen = frozenset()
# 字典内涵
import os
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}

