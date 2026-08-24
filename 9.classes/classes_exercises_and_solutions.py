from restaurant import Restaurant
from user import User

# 9.1 Restaurant demo.
trespazz = Restaurant("trespazz", "asian")
print(trespazz.name)
print(trespazz.cuisine_type)

trespazz.describe_restaurant()
trespazz.open_restaurant()
print('*' * 30)

# 9.2, 9.4 Three restaurants
ace = Restaurant("ace", "bulgarian")
porky = Restaurant("porky", "meat bbq")
trespazz = Restaurant("trespazz", "asian")

ace.describe_restaurant()
porky.describe_restaurant()
trespazz.describe_restaurant()
balkan = Restaurant("Balkan", "bulgarian food")
print(f"In restaurant \"{balkan.name}\" current served portions are {balkan.number_served}.")
balkan.served_portion = 110
print(f"In restaurant \"{balkan.name}\" current served portions are {balkan.number_served}.")
balkan.set_number_served(40)
print(f"In restaurant \"{balkan.name}\" current served portions are {balkan.number_served}.")
balkan.increment_number_served(13)
print(f"In restaurant \"{balkan.name}\" current served portions are {balkan.number_served}.")

print('*' * 30)

# 9.3 Users
Elga = User("Elga", "Ghironi", "elgaghironi77", "female", 49)
Elga.describe_user()
Elga.greet_user()
Elga.increment_login_attempts()
Elga.increment_login_attempts()
Elga.increment_login_attempts()
print(f"Logging attempts of user {Elga.username} are {Elga.login_attempts}.")
Elga.reset_logging_attempts()
print(f"Logging attempts of user {Elga.username} are {Elga.login_attempts}.")
