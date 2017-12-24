
def computepay(hours,rate):
	if float(hours) > 40: pay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5))
	else: pay = float(hours) * float(rate)
	return pay

hours = raw_input('How many hours did you work? ')
try:
	h = float(hours)
	# print 'Hours are ',h
except:
	print '\nError! Please use numbers only for the number of hours worked.\n'
	quit()

rate = raw_input('What is your rate of pay? ')
try:
	r = float(rate)
	# print 'Rate is ',r
except:
	print '\nError! Please use numbers only for the rate of pay.\n'
	quit()

pay = computepay(hours,rate)

print '\nYour pay is: $' + str(pay) +'\n'

