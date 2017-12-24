
def chop(t):
	del t[0]
	del t[-1]
	print 'chop changes it to', t
	return None

def middle(t):
	del t[0]
	del t[-1]
	return t

print ' '

b = ['a','b','c','d']
print 'b starts off as', b
b = chop(b)
print 'but chop returns', b

print ' '

c = ['a','b','c','d']
print 'c starts off as', c
c = middle(c)
print 'after middle, c is', c
print ' '
