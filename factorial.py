#program to find out the factorial of a number
#getting a number from user


def factorial(number):
	fact = 1
	for i in range(1, number+1, 1):
		fact = fact * i	
	return fact


number = int(input(" Enter a number to find the factorial"))
print (factorial(number))



