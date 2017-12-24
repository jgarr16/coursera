# this program revises the one from Chapter9 ex5.py. It counts the distribution of the hour of the day for each of the messages. To do so, it pulls the hour from the 'From' line by finding the time string and then splitting that string into parts using the colon character. Once it has accumulated the counts for each hour, it prints out the counts, one per line.

fname = raw_input('Enter a file name: ')
try:
	fhand = open(fname)
except:
	print 'Sorry, can\'t find that file. Please try again.'
	exit()

daycount = dict()
for line in fhand:
    words = line.split()
    if (len(words) >= 5) and (words[0] == 'From'): 
		domain = words[5].split(':')
		# print domain[0]      # just for testing, feel free to delete
		if domain[0] not in daycount: daycount[domain[0]] = 1
		else: daycount[domain[0]] += 1

# sort the dict() by value
lst = list()
for time, count in daycount.items():
	lst.append((time, count))

	lst.sort(reverse=False)
	
for time, count in lst:
	print time, count


