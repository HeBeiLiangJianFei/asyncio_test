#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 11:26
# @Author    : LJF
# @File      : bind_callback.py
# @CopyRight : known51
# ----------------------------------------------
import functools
import time
import asyncio

"""
绑定回调，在task执行完毕的时候可以获取执行的结果，
回调的最后一个参数是future对象，通过该对象可以获取协程返回值,
future.result()

"""

now = lambda : time.time()


async def do_some_work(x):
    print("Waiting:", x)
    return "Done after {}s".format(x)


# def callback(future):
#     print('Callback: ', future.result())


def callback(t, future):
    print('Callback:', t, future.result())


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
"""
可以看到，coroutine执行结束时候会调用回调函数。并通过参数future获取协程执行的结果。
我们创建的task和回调里的future对象，实际上是同一个对象。
"""
# task.add_done_callback(functools.partial(callback, 2))
loop.run_until_complete(task)
"""
回调一直是很多异步编程的恶梦，程序员更喜欢使用同步的编写方式写异步代码，
以避免回调的恶梦。回调中我们使用了future对象的result方法。前面不绑定回调的例子中，
我们可以看到task有fiinished状态。在那个时候，可以直接读取task的result方法
"""
print('Task ret: {}'.format(task.result()))
print("TIME:", now() - start)



