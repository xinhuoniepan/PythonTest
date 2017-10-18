#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python模块
'''
import math;
import time;
Money = 2000;
def AddMoney():
	global Money;
	Money = Money + 1;
print Money;
AddMoney();
print Money;

content = dir(math);
timeTuple = dir(time);
print content;
print timeTuple;

str = raw_input("please input num");
print "your num is :",str;

str = input("qingshuru");
print str

fo = open("test.py")
print "file name:",fo.name
print "colse?:",fo.closed
print "module:",fo.mode
print "space:",fo.softspace

fo = open("foo.txt","wb")
fo.write("7894564\n");

fo.close()

fo = open("foo.txt","r+")
str = fo.read(5);
print str;
fo.close()

os.rename("foo.txt","too.txt")
os.remove("too.txt")
os.mkdir("test")

import os;

print os.getcwd()
os.rmdir("test")
'''
def temp_convert(var):
	try:
		return int(var)
	except ValueError,Argument:
		print "parameter is not num",Argument

temp_convert("xyz");
