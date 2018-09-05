#lambda expressions, map and filter
#program to check even and odds from a list
import sys
def even_odd(num):
	if num%2==0:
		return "Even"
	else:
		return'ODD'
my_list=range(1,10)
print(my_list)
print(list(map(even_odd, my_list)))

#program to return even values from a list
def even(num):
	return num%2==0

print(list(filter(even, my_list)))

#lambda expression
#program to return square of each element of list

print(list(map(lambda num:num**2,my_list)))

#program to return square of even mumbers from the list

print(list(filter(lambda num:num%2 == 0, my_list)))
