#program to find a count of a word in a given string
my_string = input("Enter a string\n")
my_word = input("Enter a word\n")
count = 0
for word in my_string.split():
	if word.upper() == my_word.upper():
		count+=1
print("Count of word " + my_word + " = " + str(count))
