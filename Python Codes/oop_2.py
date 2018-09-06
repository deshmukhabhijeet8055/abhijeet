#Inheritence, polymorphism and abstract classes 

#Class Machine is an abstract class
class Machine():

	def __init__(self, name):
		self.name = name

	def get_type(self):
		raise NotImplementedError("Subclass should implement this abstract method")

	def get_sound(self):
		raise NotImplementedError("Subclass should implement this abstract method")

#Class Bike inherits abstract Machine class
class Bike(Machine):

	def get_type(self):
		print("\n {} is of type Two Wheeler".format(self.name))

	def get_sound(self):
		print("\n {} sounds like Vrooooom".format(self.name))

#Class Car inherits abstract Machine class
class Car(Machine):

	def get_type(self):
		print("\n {} is of type Four Wheeler".format(self.name))

	def get_sound(self):
		print("\n {} sounds like Brooooom".format(self.name))


#Implementing polymorphism in above classes

def vehicle_check(vehicle):
	vehicle.get_type()
	vehicle.get_sound()

#Creating instance of Bike and Car Objects

my_car = Car('Swift')
my_bike = Bike('Deluxe')

#Calling vehicle_check function to check the car and bike

for vehicle in [my_car, my_bike]:
	print(vehicle)
	vehicle_check(vehicle)

#End of program