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