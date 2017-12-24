# the py program will prompt for a file (mbox-short.txt) and read through it, 
# looking for a particular line of text. 

counter = 0
cumNumber = 0

fname = raw_input('Enter the file name: ')
if fname == 'na na boo boo':
	print "NA NA BOO BOO TO YOU - You have been punk'd!"
	exit()
else:
	try:
		fhand = open(fname)
	except:
		print 'File cannot be opened: ', fname
		exit()

for line in fhand:
	if line.startswith('Subject:'):
		counter = counter + 1

# print 'cumNumber = ' + str(cumNumber)
# print 'count = ' + str(counter)
print 'There were', counter,'subject lines in',fname

