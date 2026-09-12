#  10.6 Addition. Get two user-defined numbers, sum them and print them on the console. If there is a ValueError catch it.

try:
    number_one = int(input("What is your first number? "))
    number_two = int(input("What is your second number? "))
    sum_of_the_two_numbers = number_one + number_two
except ValueError:
    print("Please, enter a valid number!")
else:
    print(sum_of_the_two_numbers)
