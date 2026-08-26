from restaurant import Restaurant
from user import User
from ice_cream_stand import IceCreamStand
from admin import Admin
from privileges import Privileges

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

# 9.3, 9.5 Users
Elga = User("Elga", "Ghironi", "elgaghironi77", "female", 49)
Elga.describe_user()
Elga.greet_user()
Elga.increment_login_attempts()
Elga.increment_login_attempts()
Elga.increment_login_attempts()
print(f"Logging attempts of user {Elga.username} are {Elga.login_attempts}.")
Elga.reset_logging_attempts()
print(f"Logging attempts of user {Elga.username} are {Elga.login_attempts}.")

list_of_privileges = ["can add post", "can delete post", "can ban user", "can add/update/delete user"]
admin_privileges = Privileges(list_of_privileges)
admin = Admin("Zahari", "Styoanov",
              "zaho", "male",
               33, 0,
               Privileges(list_of_privileges))
print(f"All privileges on user @{admin.username} are as follows: ")
admin.show_privileges()
print('*' * 30)

# 9.6 Ice Cream Stand
ice_cream_flavors = ["vanilla", "chocolate", "strawberry", "blackberries", ]
my_local_stand = IceCreamStand("Palauzovo", "ice cream", 30,ice_cream_flavors )
my_local_stand.print_all_icecream_flavors()