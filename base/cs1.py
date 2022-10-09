import time
print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime()))
st = time.localtime()
print(st)
import turtle
turtle.speed(8)
turtle.hideturtle()
turtle.color('red', 'yellow')
turtle.begin_fill()
for i in range(36):
    turtle.fd(100)
    turtle.left(70)
turtle.end_fill()
turtle.done()
import random
'''
print(random.randint(1, 9))
print(random.random())
print(random.randrange(0, 8, 2))
'''
'''
str = 'hello'
print(random.choice(str))
listnum = ['1X', 'w', 'r', 'AAA']
random.shuffle(listnum)
print(listnum)
'''
import jieba
aa = jieba.lcut('北京大学的学生')
bb = jieba.lcut('北京大学的学生', cut_all=True)
cc = jieba.lcut_for_search('北京大学的学生')
print(aa)
print(bb)
print(cc)
print(jieba.lcut('北京大学的学生创业难版'))
jieba.add_word('创业难')
print(jieba.lcut('北京大学的学生创业难版'))

# import turtle
# turtle.screensize(600, 600, 'yellow')
# turtle.setup(800, 600, 0, 0)
"""
turtle.speed(10)
for i in range(1, 200, 4):
    turtle.forward(i)
    turtle.left(90)
turtle.done()
"""
'''
import turtle
# turtle.hideturtle()
turtle.color('red', 'blue')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.done()
'''
'''
import turtle
turtle.color('red', 'yellow')
turtle.speed(10)
turtle.begin_fill()
for i in range(9):
    turtle.forward(200)
    turtle.left(160)
turtle.end_fill()
turtle.done()
'''
# time
# import time
'''
st = time.localtime()
print(st)
print(type(st))
print('今天是{}月{}日'.format(st.tm_mon, st.tm_mday))

print(time.ctime())
print(time.strftime('%Y-%m-%d %H:%M:%S %a %A %b %B'))  # a 表示周几 b 表示几月
print(time.strftime('%Y-%m-%d %I:%M:%S %p'))  # p 表示 am 还是 pm
print(time.strftime('%Y-%m-%d %H:%M:%S %w %W'))  # W 表示是今年第几周 w 表示周几
'''
'''
# s1 = time.perf_counter()
s1 = time.time()
print('time')
time.sleep(3)
print('end')
s2 = time.time()
# s2 = time.perf_counter()
print(f'耗时{s2-s1}秒')
'''
'''
# 结构化对象 -> 时间戳
st = time.localtime()
print(time.mktime(st))
'''
'''
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
'''
'''
# 字符串 -> 时间结构体
strtime = '2020-07-25 13:12:18'
print(time.strptime(strtime, '%Y-%m-%d %H:%M:%S'))
'''

