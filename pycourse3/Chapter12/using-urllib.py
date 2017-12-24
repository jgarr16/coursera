# this program acts as a simple web server

import urllib

fhand = urllib.urlopen('http://data.pr4e.org/romeo.txt')
print
for line in fhand:
	print line.strip()
print