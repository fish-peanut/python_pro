# import time
#
# name_list = ['aaa', 'bbb', 'ccc', 'ddd']
#
#
# def get_name(name):
#     print("正在爬取:", name)
#     time.sleep(2)
#     print('爬取完成:', name)
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     for i in range(len(name_list)):
#         get_name(name_list[i])
#     end_time = time.time()
#     print("%d  seconds" % (end_time-start_time))


from multiprocessing.dummy import Pool
"""multiprocessing.dummy 是multiprocessing的一个子库,
    二者的不同之处就是前者应用于线程后者主要应用于进程,
    而它们实现并行化操作的关键则是map函数。
"""
# 线程池处理耗时且阻塞的操作
import time

name_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']


def get_name(name):
    print("正在爬取:" + name)
    time.sleep(2)
    print('爬取完成:' + name)
    return name


if __name__ == "__main__":
    start_time = time.time()
    pool = Pool(4)
    return_list = pool.map(get_name, name_list)
    print(return_list)
    end_time = time.time()
    print("%d  seconds" % (end_time-start_time))
