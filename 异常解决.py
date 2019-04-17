#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 10:10
# @Author    : LJF
# @File      : 异常解决.py
# @CopyRight : known51
# ----------------------------------------------

import time, asyncio, aiohttp

url = "https://www.baidu.com/{}"

tasks = []


async def hello(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print("Hello world:{}".format(time.time()))
                return await response.read()


async def fun():
    # 限制并发量
    semaphore = asyncio.Semaphore(500)
    # 列表推导式
    to_get = [hello(url.format(i), semaphore) for i in range(1000)]
    # to_get = []
    # for i in range(1000):
    #     d = asyncio.ensure_future(hello(url.format(i), semaphore))
    #     to_get.append(d)
    result = await asyncio.gather(to_get)
    print(result)


if __name__ == '__main__':
    lop = asyncio.get_event_loop()
    lop.run_until_complete(fun())
    lop.close()