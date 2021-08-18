# coding:utf-8


from datetime import datetime
from datetime import timedelta
import time

import calendar

d = datetime.now()

s = d.strftime('%Y-%m-%d %H:%M:%S')


print(s, type(s))
p = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

print(p, type(p))


timestamp = datetime.timestamp(d)

print('-------',timestamp)


for i in range(10):
    print(i)
    time.sleep(0.1)



cal = calendar.month(2021, 10)
print ("以下输出2016年1月份的日历:")
print (cal, type(cal))

l = list(cal)

print(l)


ticks = time.time()
local = time.localtime(ticks)

localtime = time.asctime(time.localtime(time.time()))
print(ticks, local, localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

