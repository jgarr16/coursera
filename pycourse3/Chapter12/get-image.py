# this program acts as a simple web server - it makes a connection to a web server and follows the rules of HTTP to request a document and display what the server sends back

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n') 

count = 0
picture = "";
while True:
	data = mysock.recv(5120)
	if (len(data) <1):
		break
	# time.sleep(0.25)
	count = count + len(data)
	print len(data), count
	picture = picture + data
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
print 'Header length', pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture);
fhand.close()