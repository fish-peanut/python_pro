import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    # 获取当前事件循环。
    loop = asyncio.get_running_loop()
    # 创建一个future对象,没绑定任何行为,则这个任务永远不知道什么时候结束.
    fut = loop.create_future()
    # 手动绑定了set_after函数,fut执行结果出来后可以结束.
    await loop.create_task(set_after(fut))
    # 等待Future对象获取最终结果,否则就会一直等待下去.
    data = await fut
    print(data)


asyncio.run(main())
