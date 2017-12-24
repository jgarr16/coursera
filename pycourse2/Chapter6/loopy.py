# both of the following do the same thing; they loop through the word 
# assigned to a variable and print it out letter by letter

fruit = 'banana'

# easy way, using built in function
for letter in fruit:
	print letter


index = 0 
while index < len(fruit):
	letter = fruit[index]
	print letter
	index = index + 1

