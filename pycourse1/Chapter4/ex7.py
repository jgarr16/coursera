# prompt for a score between 0.0 and 1.0. If the score is out of range,
# print an error message. If the score is between 0.0 and 1.0, 
# print a grade using the following table:
#
# score     grade
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

def computegrade(score):
	if float(score) > 0.0 and float(score) < 0.6: grade = 'F'
	elif float(score) >= 0.6 and float(score) < 0.7: grade = 'D'
	elif float(score) >= 0.7 and float(score) < 0.8: grade = 'C'
	elif float(score) >= 0.8 and float(score) < 0.9: grade = 'B'
	elif float(score) >= 0.9 and float(score) < 1.0: grade = 'A'
	return grade

score = raw_input('Enter the score: ')

try:
	s = float(score)
	if s > 1.0: 
		print 'Did you forget the decimal?'
		quit()
except:
	print 'Bad score, try again.'
	quit()

grade = computegrade(score) 

print 'Your grade is',grade


