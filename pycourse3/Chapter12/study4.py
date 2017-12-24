# this program reads a file and manipulates the text using RegEx (re)

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('^Details:.*rev=([0-9]+)', line)
	conf = list()
	if len(x) > 0:
		print x