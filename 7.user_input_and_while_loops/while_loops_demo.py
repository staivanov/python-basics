# # While loop intro
index = 0
end_index = 10

while index <= end_index:
    print(f"Current index is {index}")
    index += 1

print("*" * 30)

# # # Using a break
message: str = f"Enter the name of a city you have visited.\n"
message += "Enter `quit` when you are finished.\n"
quit_command: str = "quit"

while True:
    city: str = input(message)

    if city == quit_command:
        break
    else:
        print(f"I will go to {city.title()}")

print("*" * 30)

# Using a Flag
message_to_the_user: str = "Enter some text to print it on the console.\n"
active: bool = True

while active:

    message: str = input(message_to_the_user)

    if message == quit_command:
        active: bool = False
    else:
        print(message)

print("*" * 30)

# Removing All instances of specific values from a List

cities: list[str] = ["Gabrovo", "Varna", "Plovdiv", "Smolyan", "Gabrovo", "Veliko Tarnovo", "Gabrovo", "Sofia",
                     "Silistra"]
print(cities)
city_for_removing: str = "Gabrovo"

while city_for_removing in cities:
    cities.remove(city_for_removing)

print(cities)
