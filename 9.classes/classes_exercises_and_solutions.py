from restaurant import Restaurant
from user import User

# 9.1 Restaurant demo.
trespazz = Restaurant("trespazz", "asian" )
print(trespazz.name)
print(trespazz.cuisine_type)

trespazz.describe_restaurant()
trespazz.open_restaurant()
print('*' * 30)

# 9.2 Three restaurants
ace = Restaurant("ace", "bulgarian" )
porky = Restaurant("porky", "meat bbq" )
trespazz = Restaurant("trespazz", "asian" )

ace.describe_restaurant()
porky.describe_restaurant()
trespazz.describe_restaurant()

print('*' * 30)

# 9.3 Users
Elga = User("Elga", "Ghironi", "elgaghironi77", "female", 49)
Elga.describe_user()
Elga.greet_user()