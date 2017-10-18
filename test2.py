#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python列表
list = ['runoob',786,2.23,'john',70.2]
tinylist = [123,'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist * 2
#Python元组
tuple = ('runoob',786,2.23,'john',70.2)
tinyyuple = (123,'john')

list[2] = 1000
print list
#Python字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'john','code':6734,'dept':'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()
type(tinydict)

#Python 条件语句
a = 10
if(a==10):
	print("aaa")
else:
	print("bbbb")


#While语句
numberlist = [12,37,5,42,8,3]
even = []
odd = []
while (len(numberlist) > 0):
	number = numberlist.pop();
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
print(even)
print(odd)
#猜数字大小
'''
import random
s = int(random.uniform(1,10))
m = int(input('please input num:'))
while m!= s:
	if(m>s):
		print("MAX")
		m = int(input('please input num:'))
	elif(m<s):
		print("MIN")
		m = int(input('please input num:'))
	else:
		print("OK")
		break;
'''
#for循环
n = 0
for a in 'Python':
	n+=1
	if(a=='n'):
		print a,n

fruits = ['banana','apple','mango']
for index in range(len(fruits)):
	print 'now fruit:',fruits[index]

print "Good bye"
#打印一定范围内不重复的质数
for num in range(1,100):
	x = 0
	list = []
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			a = i
			if a not in list:
				list.append(i)
				list.append(j)
				print '%d = %d * %d' % (num,i,j)
			x = 1
	else:
		if x == 0:
			print num,'zhishu'
	print "-----------------"
#enumerate内置函数进行遍历
sequence = [12, 34, 34, 23, 45, 76, 89]

for index,item in enumerate(sequence):
	print index,item

#打印空心的等边三角形
'''
rows = int(raw_input('please input row num:'))
for i in range(0, rows):
	if i <> rows-1:
		for j in range(0,rows):
			if j==rows-i-1:
				print("*"),
			else:
				print("-"),
		for x in range(rows+1,2*rows):
			if x==i+rows:
				print("*"),
			else:
				print("-"),
	else:
		for y in range(0,2*rows-1):
			if y%2 == 0:
				print("*"),
			else:
				print("-"),
	print
	'''
#打印实心的等边三角形
'''
rows = int(raw_input('please input row num:'))
for i in range(0, rows):
	for j in range(0,rows):
		if i%2==0:
			if j==rows-i-1:
				print("*"),
			else:
				print("-"),
		else:
			if j==rows-i-1:
				print("*"),
			else:
				print("-"),
	print
'''
#打印空心的等边三角形
'''
rows = int(raw_input('please input row num:'))
for i in range(0, rows):
	for j in range(0,rows):
		if j==rows-i-1:
			print("*"),
		else:
			print("-"),
	for j in range(0,rows-1):
		if j==i-1:
			print("*"),
		else:
			print("-"),

	print
'''
#打印空心的等边三角形
rows = int(raw_input('please input row num:'))
for i in range(0, rows):
	for j in range(0,2*rows-1):
		if(i!=rows-1)and( j == rows-i-1 or j == rows + i -1):
			print("*"*j),
		elif i == rows-1:
			if j%2 == 0:
				print("*"*j),
			else:
				print("-"),
		else:
			print("-"),
	print

#*字塔
i=1
#j=1
while i<=9:
   if i<=5:
      print ("*"*i)

   elif i<=9 :
      j=i-2*(i-5)
      print("*"*j)
   i+=1
else :
   print("")
