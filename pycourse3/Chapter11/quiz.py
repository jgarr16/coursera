# this program reads through and parses a file with text and numbers. Then it extracts all the numbers in the file and computes the sum of the numbers.

import re

sums = list()
fname = raw_input('Enter file: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

for line in fhand:
	line = line.rstrip()
	x = re.findall('\d+', line)
	y = len(x)
	if y > 0: 
		# print x     # this just for testing, feel free to delete
		for i in range(y):
			sums.append(int(x[i]))
print 'There are', len(sums),'values with a sum of',sum(sums)
print 


