message_prompt: str = "Please, enter your name.\n"
name: str = input(message_prompt)
greeting: str = f"Hello, {name}!"
print(greeting)

# Function int()
age: int = int(input("Please, enter your age\n"))
print(f"After ten years you would be on {age + 10}")

# Is number odd or even

message: str = "Enter your number\n"
user_number: int = int(input(message))
is_number_even: bool = user_number % 2 == 0

if is_number_even:
    print(f"Your number {user_number} is even.")
else:
    print(f"Your number {user_number} is odd.")
