#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 11:45
# @Author    : LJF
# @File      : concurrent_asyncio.py 并发
# @CopyRight : known51
# ----------------------------------------------

"""
并发和并行一直是容易混淆的概念。并发通常指有多个任务需要同时进行，
并行则是同一时刻有多个任务执行。用上课来举例就是，并发情况下是一个老师在
同一时间段辅助不同的人功课。并行则是好几个老师分别同时辅助多个学生功课。
简而言之就是一个人同时吃三个馒头还是三个人同时分别吃一个的情况，吃一个馒头算一个任务。


asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，
然后其他协程继续工作。创建多个协程的列表，然后将这些协程注册到事件循环中

使用了aysncio实现了并发。asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) ,
前者接受一个task列表，后者接收一堆task

"""

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)