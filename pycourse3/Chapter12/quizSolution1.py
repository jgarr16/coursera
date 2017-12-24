# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
counts = 0
contents = 0
# Retrieve all the content of the span tags
tags = soup('span')
for tag in tags:
    counts = counts +1
    contents = contents + int(tag.contents[0])

print counts
print contents