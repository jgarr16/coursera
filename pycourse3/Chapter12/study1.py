# this program reads a file and manipulates the text using RegEx (re)

import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^From:.+@', line):
		print line