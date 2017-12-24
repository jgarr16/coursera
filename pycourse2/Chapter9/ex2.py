# this program categorizes the mbox-short.txt email string by the day that the message was
# sent. it will count the number of messages by the day that they were sent.

fhand = open('mbox-short.txt')
daycount = dict()
for line in fhand:
    words = line.split()
    if (len(words) >= 3) and (words[0] == 'From'): 
		if words[2] not in daycount: daycount[words[2]] = 1
		else: daycount[words[2]] += 1
print daycount
