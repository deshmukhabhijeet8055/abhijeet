#Generators in python

#Defining a generator for square of numbers between 1 to n

def create_square(n):
	for i in range(1, n):
		yield(i)

#Calling Generator 

for i in create_square(10):
	print(i**2)

#Taking one by one new generator object instance
print("One by one yielding numbers")
number = create_square(5)
while(1):
	try:
		print(next(number))
	except StopIteration:
		print("Generator has given the last number. Breaking the loop now")
		break
	else:
		print("Next number is as below")

