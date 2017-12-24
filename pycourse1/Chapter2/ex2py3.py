# this program prompts the user for a name and then greets them, on screen, by name. 

def namePrompt():
	name = input('What is your name? ')
	if len(name) < 1:
		print()
		print('Cat got your tongue? Try again!')
		print()
	else:
		nameResponse(name)

def nameResponse(name):
		try:
			print()
			print('Hello ' + name)
			print()
		except:
			print('Sorry, I ran into a problem there. Please try again...')
			exit()

namePrompt()

