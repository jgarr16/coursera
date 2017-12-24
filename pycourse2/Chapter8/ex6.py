# this module computes the average of a group of numbers USING a list

numlist = list()
while ( True ) :
	inp = raw_input('Enter a number: ')
	if inp == 'done' : break
	value = float(inp)
	numlist.append(value)

print 'Maximum:', max(numlist)
print 'Minimum:', min(numlist)


