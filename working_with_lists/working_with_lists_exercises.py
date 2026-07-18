# 4.1
pizzas = ["Neapolitana", "Mania", "Capricciosa"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

statement_about_pizzas = "I really like these type of pizzas from above. Recommend it to everyone."
print(statement_about_pizzas)
print("***********************")
# 4.2
raptors = ["eagle", "falcon", "hawk"]

for raptor in raptors:
    print(f"{raptor} is found on all continents except on Antarctica.")

print("Any of these animal is skilled in hunting!")
# 4.3
numbers_to_twenty = list(range(1, 21))

for number in numbers_to_twenty:
    if number <= 19:
        print(number, end=", ", flush=True)
    else:
        print(number, flush=True)
print("***********************")
# 4.4 One million
one_million = list(range(1, 1000001))
# 4.5 Summing a Million
one_million_min = min(one_million)
print("Min number in one million range of numbers is", one_million_min)
one_million_max = max(one_million)
print("Max number in one million range of numbers is", one_million_max)
sum_of_one_million_range = sum(one_million)
print("Sum of numbers one to one million is", sum_of_one_million_range)
print("***********************")
# 4.6 Odd numbers
odd_numbers_in_range = list(range(1, 21, 2))
print("All odd numbers in range from 1 to 20 are", odd_numbers_in_range)
print("***********************")
# 4.7 Threes
n = 3
number_multiplied_by_n_in_range = list(number * n for number in range(3, 31))
print(number_multiplied_by_n_in_range)
print("***********************")
# 4.8-9 Cubes
cube_multiplier = 3
first_ten_cubes = list(number ** cube_multiplier for number in range(1, 11))
print("Cubes of the first ten numbers are", first_ten_cubes)
print("***********************")
#4-11
friend_pizzas = pizzas[:]
pizzas.append("Margarita")
print("My favorite pizzas are:")
for pizza in pizzas:
    if pizza == pizzas[-1]:
        print(pizza, end=" ", flush=True)
    else:
        print(pizza, end = ", ", flush = True)
print()
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    if pizza == friend_pizzas[-1]:
        print(pizza, end = " ", flush = True)
    else:
        print(pizza, end = ", ", flush = True)

