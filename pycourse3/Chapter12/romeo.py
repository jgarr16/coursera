# this module pulls in a text file (romeo.txt), splits each line, and counts the resultant
# words to give a histogram of word usage.

import string

fname = raw_input('What is the name of the text file: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

counts = dict()
for line in fhand:
	line = line.translate(None, string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1

# sort dict() by value
lst = list()
for key, val in counts.items():
	lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
	print key, val

	