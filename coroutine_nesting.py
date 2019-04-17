#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 12:29
# @Author    : LJF
# @File      : coroutine_nesting.py
# @CopyRight : known51
# ----------------------------------------------
"""
使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程，
这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来

使用asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果

不在fun协程函数里处理结果，直接返回await的内容，
那么最外层的run_until_complete将会返回main协程的结果。

"""

import asyncio
import time

now = lambda :time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


async def fun():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    # dones, pendings = await asyncio.wait(tasks)
    # for task in dones:
    #     print("Task ret: ", task.result())

    # 使用asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print("Task ret: ", result)

    # 不在fun协程函数里处理结果，直接返回await的内容，
    # 那么最外层的run_until_complete将会返回main协程的结果。
    return await asyncio.gather(*tasks)


start = now()
loop = asyncio.get_event_loop()
results = loop.run_until_complete(fun())
for result in results:
    print("Task ret: ", result)
print("TIME: ", now() - start)