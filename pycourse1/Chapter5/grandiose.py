# this module simulates the max() function in Python

largest = None
print 'Initial: ', largest
for itervar in [3, 41, 12, 9, 74, 15, 5, 39, 16, 52, 47, 21, 66, 92, 49, 30, 94, 81, 10, 5]:
	if largest is None or itervar > largest:
		largest = itervar
	print 'Loop: ',itervar, largest
print 'Largest: ',largest
