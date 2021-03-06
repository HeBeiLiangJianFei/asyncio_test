#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 12:44
# @Author    : LJF
# @File      : coroutine_stop.py
# @CopyRight : known51
# ----------------------------------------------

"""
上面见识了协程的几种常用的用法，都是协程围绕着事件循环进行的操作。
future对象有几个状态：

Pending
Running
Done
Cancelled

创建future的时候，task为pending，事件循环调用执行的时候当然就是running，
调用完毕自然就是done，如果需要停止事件循环，就需要先把task取消。
可以使用asyncio.Task获取事件循环的task


"""
import asyncio

import time

now = lambda: time.time()


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(2)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

start = now()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print("TIME:", now()-start)


