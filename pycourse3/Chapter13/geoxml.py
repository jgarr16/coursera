import urllib
import xml.etree.ElementTree as ET


address = raw_input('Enter location: ')
# address = 'http://python-data.dr-chuck.net/comments_42.xml'

url = address
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
summer = 0

for item in lst:
	summer = summer + int(item.find('count').text)
print summer


# results = tree.findall('commentinfo')
# nums = results.find('comments').find('comment').find('count').text
#counts = tree.findall('tree')
# lng = results[0].find('geometry').find('location').find('lng').text
# location = results[0].find('formatted_address').text
#print count
# print 'nums: ',nums
# print location