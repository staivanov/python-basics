from restaurant import Restaurant
from user import User
from ice_cream_stand import IceCreamStand
from admin import Admin
from privileges import Privileges
from dice import Die
from random import randint

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
my_local_stand = IceCreamStand("Palauzovo", "ice cream", 30, ice_cream_flavors)
my_local_stand.print_all_icecream_flavors()
print('*' * 30)

# 9.13 Dice. Make a new class Die with attribute sides and method roll_die. Call it 10 times.
new_die = Die(6)
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()

print('*' * 30)

# 9.14 Lottery. Make a lottery source represented with tuple with 10 numbers and 5 letters. Randomly select 4 items from the tuple representing a winner ticket.
lottery_source = (78, 'M', 79, 'S', 63, 'M', 99, 'I', 99, 'K', 25, 48, 11, 53, 74)


def draw_a_winning_combination(source: tuple):
    """ This function is a simple random generator of items from a tuple as a source. Evey element can be drawn more than once."""
    min_random_number = 0
    max_random_number = int(len(source)) - 1
    first_draw = 1
    last_draw = 4
    winning_ticket_combo = []

    while first_draw <= last_draw:
        current_random_index = randint(min_random_number, max_random_number)
        winning_ticket_combo.append(source[current_random_index])
        first_draw += 1

    return winning_ticket_combo


winning_ticket_combination = ()
winning_ticket_combination = draw_a_winning_combination(lottery_source)
print(winning_ticket_combination)
