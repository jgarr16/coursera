hours = raw_input('How many hours did you work? ')
h = float(hours)
rate = raw_input('What is your rate of pay? ')
r = float(rate)

if h > 40: pay = (40 * r) + ((h - 40) * (r * 1.5))
else: pay = float(hours) * float(rate)

print '\nYour pay is: $' + str(pay) +'\n'