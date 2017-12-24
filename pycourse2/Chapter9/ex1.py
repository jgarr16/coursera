# program reads words from words.txt, stores them as keys in a dictionary, and then
# uses 'in' to check whether specific words (strings) exist in the dict.

words = dict()
count = 0

# print words

fhand = open('words.txt')
for line in fhand:
	xwords = line.split()
	# print xwords
	for x in range(len(xwords)):
		if x in words: continue
		else: words[xwords[x]] = ''
		
print '\n',words,'\n'
testy = 'assistants' in words
print testy,'\n'



