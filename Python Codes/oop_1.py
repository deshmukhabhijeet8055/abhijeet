#object oriented programming in python

class Dog:

	def __init__(self, name, breed = 'Lab'):
		self.breed = breed
		self.name = name

	def __str__(self):
		return self.name

my_dog_1 = Dog(breed = 'German Shefered', name = 'Tommy')
my_dog_2 = Dog(name = 'Jack')
my_dog_3 = Dog(name = 'Sammy')

dog_list = [my_dog_1, my_dog_2, my_dog_3]
print(dog_list)

#Printing the dog names using str overriding
print(list(map(lambda name:name.name, dog_list)))

#Pring the dog name and breed for all the dogs
for dog in dog_list:
	print('{} is a {}'.format(dog.name,dog.breed))

