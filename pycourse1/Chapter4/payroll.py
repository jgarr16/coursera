def computepay(h,r):
    if h > 40: pay = (40 * r) + ((h - 40) * (r * 1.5))
    else: pay = h * r
    return pay

hrs = raw_input("Enter Hours:")
try:
    h = float(hrs)
except:
    print 'bad input'
    quit()
rate = raw_input("Enter Rate: ")
try:
    r = float(rate)
except:
    print 'bad input'
    quit()

p = computepay(h,r)
print p