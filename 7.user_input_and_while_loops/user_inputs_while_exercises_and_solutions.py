# 7.1 Rental car
message_to_the_user = "What car do you want to rent?\n"
car = input(message_to_the_user)
print(f"Let me see if I can find you a {car}")
print("***********************************")

# 7.2 Restaurant Seating

message_to_the_user = "How many people are in your dinner group?"
answer = int(input(message_to_the_user))

if answer > 7:
    print("You have to wait for a table.")
else:
    print("Your table is ready.")

print("***********************************")

# 7.3 Multiple Of 10
number = int(input("Enter your number\n"))

if number % 10 == 0:
    print(f"Yes, your number {number} is multiple of 10.")
else:
    print(f"No, your number {number} is not multiple of 10.")

# 7.4 Pizza toppings
pizza_toppings = []
pizza_topping = ""

while True:
    pizza_topping = input("Please, enter your pizza topping.\n")

    if pizza_topping.lower() != "quit":
        pizza_toppings.append(pizza_topping.lower())
    else:
        break

print(pizza_toppings)
print("***********************************")

# 7.5 Movie tickets prices according the age.
toddler = 3
child = 12
teen = 15
child_ticket = 10
adult_ticket = 15
message_to_the_user = "Please, enter your age bellow.\n"
age = 0

while True:  # It's an Infinite loop
    print(message_to_the_user)
    age = int(input())

    if age < 3:
        print("Your ticket is free. Enjoy the LiFE!!!")
    elif toddler <= age <= child:
        print(f"Price for your ticket is {child_ticket}")
    elif age > child:
        print(f"Price for your ticket is {adult_ticket}")

# 7.8 Deli

sandwich_orders = ["pastrami", "tuna", "four type cheese", "pastrami", "ol\' American hot", "pastrami",
                   "brazil sausage with Pao de queijo"]
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

for sandwich_ready in finished_sandwiches:
    print(f"\t{sandwich_ready}")

# 7.9 No pastrami

print("The Deli has run out of pastrami!")
pastrami = "pastrami"

while pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami)

print(f"Current list with all sandwiches: {sandwich_orders}")
