# this program reads a file and prints the letters in decreasing order of frequency. It converts all the input to lower case and only counts the letters a-z. It does not count spaces, digits, punctuation, or anything other than the letters a-z. 

fname = 'words.txt'
fhand = open(fname)
# fname = raw_input('Enter a file name: ')
# try:
# 	fhand = open(fname)
# except:
# 	print 'Sorry, can\'t find that file. Please try again.'
# 	exit()

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


