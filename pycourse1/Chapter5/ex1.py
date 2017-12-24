largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" : break
	try:
		i = int(num)
		if smallest is None or i < smallest:
			smallest = i

		if largest is None or i > largest:
			largest = i
			continue

	except:
		print 'Invalid input'
		continue
print "Maximum is", largest
print "Minimum is", smallest