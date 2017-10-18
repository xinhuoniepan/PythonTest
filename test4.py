#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python函数

def printme(str):
	print str
	return

printme(123)

#Python传不可变对象
def ChangeInt ( a ):
	a = 10;
	return a
b = 2;
c=ChangeInt(b);
print c;
print b;



# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist


#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
 
#调用printinfo函数
printinfo( age=50, name="miki" );


def printinfo (name ,age):
	print "name:",name;
	print "age:",age;
	return;

printinfo("sam",0);


def printinfo1( *name):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age ", age;
   return;
printinfo("sam",0);
