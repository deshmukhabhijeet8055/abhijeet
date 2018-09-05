#Take input string from user. Check if a word starts with "a" in the string. If found add 'bb' at the front of the word.
my_string = input("Enter a string of your choice.\n")
s_list = my_string.split()
for word in enumerate(s_list):
	if (word[1][0] == 'a') or (word[1][0] == 'A'):
		s_list[word[0]] = 'bb' + s_list[word[0]]


print(s_list)