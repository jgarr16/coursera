# this program prompts for a web address, opens the web page, reads the data and passes it to the BeautifulSoup parser, and then retrieves all anchor tags


import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	# look at the parts of a tag
	print 'TAG:',tag
	print 'URL:',tag.get('href', None)
	print 'Content:',tag.contents[0]
	print 'Attrs:',tag.Attrs
