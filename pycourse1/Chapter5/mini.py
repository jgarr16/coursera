# this exercise simulates the min() function in Python

smallest = None
print 'Initial: ', smallest
for itervar in [3, 41, 12, 9, 74, 15, 5, 39, 16, 52, 47, 21, 66, 92, 49, 30, 94, 81, 10, 5]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print 'Loop: ',itervar, smallest
print 'Smallest: ',smallest
