#list comprehension
#Creating a list of number from 1 to 10.

my_list = [ num**2 for num in range(1,11) if num%2==0]
print(my_list)