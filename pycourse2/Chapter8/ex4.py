# ex4 opens romeo.txt, reads it line-by-line and parses out each word
# then creates a list of individual words contained in the file
# then prints the resulting words in alphabetical order

romeoWords = []
count = 0
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()
	count = len(words)
	# print len(words)
	for cnt in range(count):
		if words[cnt] not in romeoWords: 
			romeoWords.append(words[cnt])
	

print sorted(romeoWords)