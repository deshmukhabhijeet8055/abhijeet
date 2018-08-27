#program to take values from user and turn them into a list and tuple
#comment added
values = str(input("Enter some comma seperated values"))
my_list = values.split(",")
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
