# this program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.

import urllib
import json

address = raw_input('Enter location: ')    # http://python-data.dr-chuck.net/comments_42.json
print 'Retrieving', address
counter = 0
sums = list()

uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved', len(data), 'characters' 
info = json.loads(data)

while True:
	# print info['comments'][(counter)]['count']
	try:
		# print int(info['comments'][(counter)]['count'])
		sums.append(int(info['comments'][(counter)]['count']))
		counter = counter + 1
	except:
		break
		

print 'Count:',counter
print 'Sum:',sum(sums)