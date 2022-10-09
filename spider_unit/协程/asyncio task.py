import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


# async def main():
#     print('main 开始')
#
#     tasklist = [
#         asyncio.create_task(func(), name='task-1'),
#         asyncio.create_task(func(), name='task-2')
#     ]
#
#     print('main 结束')
#
#     done, pending = await asyncio.wait(tasklist)
#     print(done)
#
#
# asyncio.run(main())


tasklist = [
    func(),
    func()
]

asyncio.run(asyncio.wait(tasklist))

