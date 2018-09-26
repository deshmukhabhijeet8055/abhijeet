#decorators in python

#Decorator Fuction definition
def my_decorator(original_func):

	def decorated_function():
		#Before original Function call
		print("I am being called before original function call")
		#Calling function
		original_func()
		#After original Function call
		print("I am being called after original function call")

	return decorated_function


#Creating an original function
@my_decorator
def org_func(name='abhijeet'):
	print("My name is {}".format(name))

#Calling original Fucntion

org_func()