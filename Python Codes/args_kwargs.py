#*args and kwargs understanding
import sys
def numbers(*args, **kwargs):
	'''
	DOCSTRING: This funtion returns the square of numbers passed.
	'''
	squared_list = [x**2 for x in args]
	print("My dictionary = {}".format(kwargs))
	print(squared_list)
	print("Number is {} and fruit is {}".format(args[3],kwargs['fruit']))

numbers(1, 2, 3, 4, 5,fruit='Apple',animal='cat')
