import datetime


def test():
    for i in range(10):
        yield i


a = test()
for i in a:
    print(i)
