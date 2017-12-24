# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))+1
position = int(raw_input('Enter position: '))-1
urllist = list()
# print count
# print url

for i in range(int(count)):
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	tags = soup('a')
	for tag in tags:
		urllist.append(tag.get('href', None))
	# print urllist[int(position)]
	url = urllist[int(position)]
	urllist = []
	# print '# 2',url

