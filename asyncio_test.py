#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 8:58
# @Author    : LJF
# @File      : asyncio_test.py
# @CopyRight : known51
# ----------------------------------------------

import asyncio
import time


async def hello():
    """
    异步函数：async def 用来定义异步函数，其内部有异步操作。
    每个线程有一个事件循环，主线程调用asyncio.get_event_loop()时会创建事件循环，
    你需要把异步的任务丢给这个循环的run_until_complete()方法，事件循环会安排协同程序的执行。
    :return:
    """
    asyncio.sleep(1)
    print("Hello world:{}".format(time.time()))


def fun():
    for i in range(5):
        loop.run_until_complete(hello())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fun()
    loop.close()