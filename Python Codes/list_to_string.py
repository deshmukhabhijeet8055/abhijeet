#program to concatenate all the contains of list into a string
my_list = ['what', 'is', 'name', 'of', 'you']
my_string = ""

for word in my_list:
	my_string = my_string + " " + word

print(my_string)