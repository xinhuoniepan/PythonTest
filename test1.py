#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 1、hello world
print 'hello';print 'world';
# 2、缩进
if True:
    print "True"
else:
	print "False"
#用户输入按回车后退出
#raw_input("\n\nPress the enter key to exit.")

import sys;x = 'runoob';sys.stdout.write(x + '\n')

#print输出
x='a'
y='b'
print x
print y
print "---------"
print x,
print y
print "---------"
print x,y

#变量赋值
counter = 100
miles = 1000.0
name = "John"
print counter,miles,name
#多个变量赋值
a = b = c = 1
print a,b,c

a,b,c = 1,2,"John"
print a,b,c
#Python数字
var1 = 1
var2 = 10
print var1,var2
del var1,var2
#print var1,var2
#Python字符串
s = "watashinohatsukoi"
print s
#Python列表
list = ['runoob',786,2.23,'john',70.2]
tinylist = [123,'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist
