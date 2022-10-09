import aiohttp
import asyncio
import time

start = time.time()
urls = []


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # 可用get,post
        # headers, proxy = '', 这里不用proxies, proxy直接用字符串
        async with await session.get(url) as response:
            # 文本用text(), 二进制数据用read(), json直接用json()
            page_text = await response.text()
            print(page_text)


tasks = [get_page(url) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end - start)

