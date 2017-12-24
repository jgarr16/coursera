# this program acts as a simple web server

import urllib

counts = dict()
fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
print counts
