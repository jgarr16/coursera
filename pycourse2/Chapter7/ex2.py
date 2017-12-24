# the py program will prompt for a file (mbox-short.txt) and read through it, 
# looking for a particular line of text. 

counter = 0
cumNumber = 0

fname = raw_input('Enter a file name: ')
try:
	fhand = open(fname)
except:
	print '\nSorry, that file does not exist. Please try again.\n'
	exit()

for line in fhand:
	line = line.rstrip()
	if line.find('X-DSPAM-Confidence:') == -1 : 
		continue
	else: 
		atColon = line.find(':')
		# print 'atColon = position' + str(atColon)
		confidence = line[atColon+1:]
		try:
			number = float(confidence)
			# print number
			cumNumber = cumNumber + number
			# print cumNumber, type(cumNumber) 
		except:
			print 'Something funky here.'
		counter = counter + 1

# print 'cumNumber = ' + str(cumNumber)
# print 'count = ' + str(counter)
print 'Average spam confidence:',(cumNumber/counter)

