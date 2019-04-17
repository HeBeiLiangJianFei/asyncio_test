#  -*- coding: utf-8  -*-
# ----------------------------------------------
# @Time      : 2019/4/17 0017 9:58
# @Author    : LJF
# @File      : http_list_url.py
# @CopyRight : known51
# ----------------------------------------------

import asyncio
import time
from aiohttp import ClientSession

url = ['http://www.baidu.com', 'http://www.taobao.com', 'http://www.jd.com',]
# tasks = []


async def get_response(url):
    """
    异步发起http请求，异步接受response
    :param url:
    :return:
    """
    async with ClientSession() as session:
        async with session.get(url) as response:
            print("Hello world:{}".format(time.time()))
            return await response.read()


async def fun():
    """
    发起循环事件
    :return:
    """
    # for i in url:
    #     tasks.append(asyncio.ensure_future(get_response(i)))
    tasks = [asyncio.ensure_future(get_response(i)) for i in url]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(fun())
    print(result)