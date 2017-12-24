# this program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum

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


