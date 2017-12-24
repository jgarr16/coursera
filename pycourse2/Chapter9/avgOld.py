# this module computes the average of a group of numbers without using a list

total = 0
count = 0

while ( True ) :
	inp = raw_input('Enter a number: ')
	if inp == 'done' : break
	value = float(inp)
	total = total + value
	count = count + 1

average = total/count
print 'Average:', average

