# this program acts as a simple web server

import socket

get_url = raw_input('Input your URL: ')   # http://data.pr4e.org/romeo.txt
try:
	domain_url = get_url.split('/')[2]
except:
	print '\nSorry, that URL doesn\'t resolve!\n'
	exit()
# print domain_url
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain_url, 80))
mysock.send('GET http://' + domain_url +' HTTP/1.0\n\n') 


while True:
	data = mysock.recv(512)
	if (len(data) <1):
		break
	print data

mysock.close()
