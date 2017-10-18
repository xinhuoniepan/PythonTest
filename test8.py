#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Python正则表达式

import re
print(re.match('www','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*) (.*) (.*)',line,re.M|re.I)
if matchObj:
	print "matchObj.group():",matchObj.group()
	print "matchObj.group(1):",matchObj.group(1)
	print "matchObj.group(2):",matchObj.group(2)
	print "matchObj.group(3):",matchObj.group(3)
	print "matchObj.group(4):",matchObj.group(4)
	print re.match(r'dogs',line,re.M|re.I)

else:
	print "No match!"

def double (matched):
	value = int(matched.group('value'))
	return str(value * 2)

s = 'A12FF589SS'
print(re.sub('(?P<value>\d+)',double,s))
	
