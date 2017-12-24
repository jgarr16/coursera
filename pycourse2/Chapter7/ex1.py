# the py program will read through a file (mbox-short.txt) and print the contents of that
# file, line-by-line, all in upper case text (as if shouting). 

fname = raw_input('Enter a file name: ')
try:
	fhand = open(fname)
except:
	print '\nSorry, that file does not exist. Please try again.\n'
	exit()
for line in fhand:
	line = line.rstrip()
	line = line.upper()
	print line
