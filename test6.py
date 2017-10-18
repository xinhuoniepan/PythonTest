#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python模块
'''
class Employee:
	'All employee'

	empCount = 0;

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary;
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
	
	def displayEmployee(self):
		print "Name:",self.name,",Salary:",self.salary
	'123456798'
emp1 = Employee("zero",2000)
emp2 = Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print hasattr(emp1,'age')
emp1.age = 7
print hasattr(emp1,'age')
print getattr(emp1,'age')
emp1.age = 8
print getattr(emp1,'age')
del emp1.age
setattr(emp1,'age',9)
print hasattr(emp1,'age')
print getattr(emp1,'age')
delattr(emp1, 'age')
print hasattr(emp1,'age')
print Employee.__doc__
print Employee.__dict__
'''
class Point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
		print x,y
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name,"delete"
pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1),id(pt2),id(pt3)
del pt1

print id(pt2),id(pt3)
