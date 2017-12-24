fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be found:', fname
	exit()
	
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'There are', count, 'subject lines in', fname

