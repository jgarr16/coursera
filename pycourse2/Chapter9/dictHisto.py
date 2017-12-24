# playing with dict() that makes a histogram

word = 'supercalafragilisticexpialadotious'
d = dict()
for c in word:
	d[c] = d.get(c,0) + 1
print d
