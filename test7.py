#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python类的继承
class Parent:
	parentAttr = 100
	def __init__(self):
		print "parent  hanshu"

	def parentMethod (self):
		print "diaoyongfuleiMethod"

	def setAttr (self,attr):
		Parent.parentAttr = attr

	def getAttr (self):
		print "fuleishuxing:",Parent.parentAttr

	def myMethod (self):
		print "parent's method"

class Mother:
	def mother (self):
		print "this is mother"

class Child(Parent,Mother):
	def __init__ (self):
		print "diaoyong zilei gouzao fangfa"

	def childMethod (self):
		print 'diaoyong zilei fangfa'

	def mother (self):
		print "this is child"

	def myMethod (self):
		print "child's method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.mother()
c.myMethod()

print issubclass(Mother,Parent)
print isinstance(Child,Parent)


class Vector:
	def __init__ (self,a,b):
		self.a = a;
		self.b = b;
	
	def __str__ (self):
		return 'Vector(%d,%d)'%(self.a,self.b)

	def __add__ (self,other):
		return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

class JustCounter:
	__secretCount = 0
	publicCount = 0

	def count (self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter._JustCounter__secretCount
'''print counter.__secretCount'''
