# Using try-except blocks

try:
    print(79 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("*" * 30)
# Using exceptions to prevent chares.

print("This is a very simple program that divide two user-defined numbers.")
print("Enter \'q\' to exit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q': break

    second_number = input("\nSecond number: ")
    if second_number == 'q': break

    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print(result)


