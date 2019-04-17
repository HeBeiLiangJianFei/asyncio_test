#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 9:20
# @Author    : LJF
# @File      : http_异步_请求.py
# @CopyRight : known51
# ----------------------------------------------

import asyncio
from aiohttp import ClientSession
import time

tasks = []
url = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # response = await response.read()
            # print(response)
            print("Hello world:{}".format(time.time()))
            return await response.read()


def fun():
    for i in range(5):
        # asyncio.ensure_future()创建一个task(任务)
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)
    # asyncio.gather()将响应全部收集起来
    # 我们使用了aysncio实现了并发。asyncio.wait(tasks)
    # 也可以使用
    # asyncio.gather(*tasks), 前者接受一个task列表，后者接收一堆task
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fun()
    """
    fun()
    # run_until_complete的参数是一个future对象，当传入一个携程，其内部会自动封装成task
    loop.run_until_complete(asyncio.wait(tasks))
    print(tasks)
    loop.close()
    """
