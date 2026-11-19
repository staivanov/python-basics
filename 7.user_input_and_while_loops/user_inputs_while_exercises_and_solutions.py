# 7.1 Rental car
message_to_the_user: str = "What car do you want to rent?\n"
car: str = input(message_to_the_user)
print(f"Let me see if I can find you a {car}")
print("*" * 30)

# 7.2 Restaurant Seating

message_to_the_user: str = "How many people are in your dinner group?"
answer: int = int(input(message_to_the_user))
is_bigger_than_sev: bool = answer > 7

if is_bigger_than_sev:
    print("You have to wait for a table.")
else:
    print("Your table is ready.")

print("*" * 30)


# 7.3 Multiple Of 10
number: int = int(input("Enter your number\n"))
is_multiple_of_ten: bool = number % 10 == 0

if is_multiple_of_ten:
    print(f"Yes, your number {number} is multiple of 10.")
else:
    print(f"No, your number {number} is not multiple of 10.")

# 7.4 Pizza toppings
pizza_toppings: list = []
pizza_topping: str = ""
quit_command: str = "quit"

while True:
    pizza_topping: str = input("Please, enter your pizza topping.\n")

    if pizza_topping.lower() != quit_command:
        pizza_toppings.append(pizza_topping.lower())
    else:
        break

print(pizza_toppings)
print("*" * 30)

# 7.5 Movie tickets prices according the age.
toddler: int = 3
child: int = 12
teen: int = 15
child_ticket: int = 10
adult_ticket: int = 15
message_to_the_user: str = "Please, enter your age bellow.\n"
age: int = 0

while True:  # It's an Infinite loop
    print(message_to_the_user)
    age: int = int(input())
    is_toddler: bool = age <= 3
    
    if is_toddler:
        print("Your ticket is free. Enjoy the LiFE!!!")
    elif toddler < age <= child:
        print(f"Price for your ticket is {child_ticket}")
    elif age > child:
        print(f"Price for your ticket is {adult_ticket}")

# 7.8 Deli

sandwich_orders: list[str] = ["pastrami", "tuna", "four type cheese", "pastrami", "ol\' American hot", "pastrami",
                   "brazil sausage with Pao de queijo"]

finished_sandwiches: list = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

for sandwich_ready in finished_sandwiches:
    print(f"\t{sandwich_ready}")

# 7.9 No pastrami

print("The Deli has run out of pastrami!")
pastrami: str = "pastrami"

while pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami)

print(f"Current list with all sandwiches: {sandwich_orders}")
