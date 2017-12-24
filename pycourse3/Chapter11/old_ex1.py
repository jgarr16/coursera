# this program revises the one from Chapter9 ex4.py. Read and parse the 'From' lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

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
		if words[1] not in daycount: daycount[words[1]] = 1
		else: daycount[words[1]] += 1

# print daycount      # this just for testing, feel free to delete

# sort the dict() by value
lst = list()
for email, count in daycount.items():
	lst.append((count,email))

lst.sort(reverse=True)

for count, email in lst[:1]:
	print email, count

# maximum = max(daycount, key=daycount.get)  # this works, but not acceptable for class solution
# print maximum, daycount[maximum]

# maximum = max(daycount.values())
# maxkey = [key for key, value in daycount.items() if value == maximum]
# print maxkey[0], maximum

