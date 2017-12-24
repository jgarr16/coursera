# this module pulls in a text file (romeo.txt), splits each line, and counts the resultant
# words to give a histogram of word usage.

fname = raw_input('What is the name of the text file: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
for key in counts:
	print key, counts[key]

	