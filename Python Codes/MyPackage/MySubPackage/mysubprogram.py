#this is a program in subpackage

def add_two_strings(string1, string2):
	print(string1 + ' ' + string2)

#Chekcing if this program is called directly or from other program.

if __name__ == '__main__':
	print("This program is being called directly")
else:
	print("This program is being called from other module")

