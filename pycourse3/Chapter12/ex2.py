# this program looks for lines of the form - New Revision: 39772 - and extracts the number from each of the lines using a regular expression and the findall() method. Then it computes the average of the numbers and prints out the average

import re

avg = list()
fname = raw_input('Enter file: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

for line in fhand:
	line = line.rstrip()
	x = re.findall('New Revision: (\d+)', line)
		# print x     # this just for testing, feel free to delete

	if len(x) > 0 :
		avg.append(float(x[0]))
		average = (sum(avg)/len(avg))
print average
print 


