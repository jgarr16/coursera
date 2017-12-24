# this program categorizes the mbox-short.txt email string by the day that the message was
# sent. it will count the number of messages by the day that they were sent.

fname = raw_input('Enter a file name: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

daycount = dict()
for line in fhand:
    words = line.split()
    if (len(words) >= 2) and (words[0] == 'From'): 
		domain = words[1].split('@')
		#print domain[1]
		if domain[1] not in daycount: daycount[domain[1]] = 1
		else: daycount[domain[1]] += 1
print daycount
