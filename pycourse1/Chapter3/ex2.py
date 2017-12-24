hours = raw_input('How many hours did you work? ')
try:
	h = float(hours)
except:
	print '\nError! Please use numbers only for the number of hours worked.\n'
	quit()

rate = raw_input('What is your rate of pay? ')
try:
	r = float(rate)
except:
	print '\nError! Please use numbers only for the rate of pay.\n'
	quit()

if h > 40: pay = (40 * r) + ((h - 40) * (r * 1.5))
else: pay = float(hours) * float(rate)

print '\nYour pay is: $' + str(pay) +'\n'