#program to understand file operations

with open('newfile.txt', mode = 'w') as f:
	f.write("This is the heading of this file.\n")
	f.write("This is second line.\n")
	f.write("This is third line.\n")

with open('newfile.txt', mode = 'r') as f:
	for word in f.readlines():
		print(word)

print("Second line of the file is")
with open('newfile.txt', mode = 'r') as f:
	for num_word in enumerate(f.readlines()):
		if num_word[0] == 1:
			print(num_word[1])
