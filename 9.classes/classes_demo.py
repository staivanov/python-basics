from dog import Dog
from restaurant import Restaurant
from car import Car

# Dog demo.
my_dog = Dog("Dark Lord", 8, "male")
neighbours_dog = Dog("Daisy", 2, "female")

my_dog.present_myself()
neighbours_dog.present_myself()
neighbours_dog.sit()
print('*' * 30)

# Restaurant demo.

trespazz = Restaurant("trespazz", "asian")
print(trespazz.name)
print(trespazz.cuisine_type)

trespazz.describe_restaurant()
trespazz.open_restaurant()
print('*' * 30)

# Car demo.

my_new_car = Car("Porsche", "911 Carrera", 2005)
print("My new car is " + my_new_car.get_description())
