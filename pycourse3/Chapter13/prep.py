import urllib
import json

counter = 0
sums = list()
address = 'http://python-data.dr-chuck.net/comments_42.json'

uh = urllib.urlopen(address)
data = uh.read()
info = json.loads(data)

print 'data - ',len(data)
print 'info -',len(info)
print "info['comments'] -",len(info['comments'])

while True:
	# print info['comments'][(counter)]['count']
	try:
		print int(info['comments'][(counter)]['count'])
		sums.append(int(info['comments'][(counter)]['count']))
		counter = counter + 1
	except:
		break
		
print sum(sums)
print counter








