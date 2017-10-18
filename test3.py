#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time;#引入time模块
import calendar;#引入日历模块
i = 2
while(i<100):
	j=2
	while(j<=(i/j)):
		if not(i%j): break
		j = j + 1
	if (j > i/j) : print i,"sushu"
	i = i + 1
print "Bye bye"


var1 = 'Hello World'
print var1[:6] + 'Runoob'
print "%%%"



#列表
numStr = ['aqw',2]
for index in range(0,len(numStr)):
	print numStr[index]*2
print min(numStr)

del numStr[0]
print numStr[0]
numStr.insert(0,'789')
print numStr
numStr.sort
print numStr

#Python日期和时间
ticks = time.time();
print ticks;
print time.localtime(ticks);
print time.asctime(time.localtime(ticks));

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

cal = calendar.month(2017)
print cal;

