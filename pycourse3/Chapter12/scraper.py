# this program scrapes a web page, extracts hyperlinks, and prints them out one-by-one

import urllib
import re

url = raw_input('Enter URL - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
	print link
	