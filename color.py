#! /usr/bin/env python
# -*- coding: utf-8 -*-

SCHEMA = '\x1b[48;5;%dm '
print 'System color:'

for color in range(8):
	print SCHEMA % color,
print '\x1b[0m'
for color in range(8, 16):
	print SCHEMA % color,
print '\x1b[0m\n'


print 'Color cube(6x6x6):'
for green in range(6):
	for red in range(6):
		for blue in range(6):
			color = 16 + red * 36 + green * 6 + blue
			print SCHEMA % color,
		print '\x1b[0m',
	print '\n',

print '\nGrayscale:'
for color in range(232, 256):
	print SCHEMA % color,
print '\x1b[0m\n'

