#coding=utf-8
import re
a = re.compile(r'(\s*\d+\.\d*)')

#m1 = a.match('5.433 3.1111')
m1 = re.match(r'(\s*)(\d+)(\.\d*)', '   3.14 4.33')
m2 = a.match('33')
m3 = a.match('3.')

if m1:
	print m1.group()
	print m1.groups()
	print m1.start(), m1.end()
else:
	print 'm1不是小数'
if m2:
	print m2.groupdict()
else:
	print 'm2不是小数'
if m3:
	print m3.group()
else:
	print 'm3不是小数'
