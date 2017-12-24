# this program simulates the operation of the grep command on Unix. It asks the user to enter a regular expression and then counts the number of lines that matched the regular expression

import re

grepreq = raw_input('Enter a regular expression: ')
#print grepreq, type(grepreq)        # this just for testing, feel free to delete
text = open('mbox.txt')
runcount = 0
try:
	for line in text:
		line = line.rstrip()
		x = re.findall(grepreq, line)
		if len(x) > 0 : 
			# print x
			# print line      # this just for testing, feel free to delete
			runcount += 1
except:
	print 'Sorry, I can\'t run that generalized regular expression parser. Please try again.'
	exit()


print 'mbox.txt had',runcount, 'lines that matched', grepreq

