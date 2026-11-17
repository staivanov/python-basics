car_brands: list[str] = ["Porsche", "BMW", "Mercedes", "Audi", "RUF", "Opel"]
for car_brand in car_brands:
    print(car_brand)
print("*" * 30)

# Making numerical lists
numbers: list[int] = list(range(1, 7))
print("List of numbers: ", numbers)
square_of_numbers: list[int] = []

for number in numbers:
    current_number_squared: int = number ** 2
    square_of_numbers.append(current_number_squared)

print("List of numbers on square from above: ", square_of_numbers)
print("*" * 30)
digits: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -11]
min_digit: int = min(digits)
max_digit: int = max(digits)
sum_of_all_digits: int = sum(digits)
print("All digits in the list are", digits)
print("Min digit is", min_digit)
print("Max digit is", max_digit)
print("Sum of all digits in the list is", sum_of_all_digits)
print("*" * 30)

## List Comprehensions
squares_v2: list[int] = [value ** 2 for value in range(1, 11)]
print("Demo for list comprehension", squares_v2)
print("*" * 30)

# Working with part of a list
argentina_football_players: list[str] = ["Musso", "Tagliafico", "Martinez", "Romero", "Otamendi", "Palacios",
                                         "Fernandez",
                                         "Alvarez", "MacAlistar", "Messi"]
print("Squat members of National football team of Argentina :", argentina_football_players)
first_three_players: list[str] = argentina_football_players[0:3]
print("First three players are", first_three_players)
print("From second to fourth are ", argentina_football_players[1:4])
print("From third to the end: ", argentina_football_players[2:])
print("Last three players are: ", argentina_football_players[-3:])

# Copy the entire list.
afa: list[str] = argentina_football_players[:]
print(afa)
print("*" * 30)

# Tuples
dimension: tuple(int) = (150, 50)
print("Dimension [0] and [1]")
print(dimension[0])
print(dimension[1])
