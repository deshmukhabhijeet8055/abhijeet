#program to understand file operations

with open('newfile.txt', mode = 'w') as f:
	f.write("This is the heading of this file.")
	f.write("This is second line")
	f.write("This is third line")

with open('newfile.txt', mode = 'r') as f:
	for word in f.readlines():
		print(word + "\n")
