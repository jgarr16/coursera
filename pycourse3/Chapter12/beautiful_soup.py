# this program prompts for a web address, opens the web page, reads the data and passes it to the BeautifulSoup parser, and then retrieves all anchor tags


import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link