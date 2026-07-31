# # While loop intro
index = 0
end_index = 10

while index <= end_index:
    print(f"Current index is {index}")
    index += 1


# print("****************************************")
# # # Using a break
message = f"Enter the name of a city you have visited.\n"
message += "Enter `quit` when you are finished.\n"

while True:
    city = input(message)

    if city == "quit":
        break
    else:
        print(f"I will go to {city.title()}")

# print("****************************************")
# Using a Flag
message_to_the_user = "Enter some text to print it on the console.\n"
active = True

while active:

    message = input(message_to_the_user)

    if message == "quit":
        active = False
    else:
        print(message)

print("****************************************")

# Removing All instances of specific values from a List

cities = ["Gabrovo", "Varna", "Plovdiv", "Smolyan", "Gabrovo", "Veliko Tarnovo", "Gabrovo", "Sofia", "Silistra"]
print(cities)
city_for_removing = "Gabrovo"

while city_for_removing in cities:
    cities.remove(city_for_removing)

print(cities)

