car_brands = ["Porsche", "BMW", "Mercedes", "Audi", "RUF", "Opel"]
for car_brand in car_brands:
    print(car_brand)
print("************************************")
# Making numerical lists

numbers = list(range(1, 7))
print("List of numbers: ", numbers)
square_of_numbers = []

for number in numbers:
    square = number ** 2
    square_of_numbers.append(square)

print("List of numbers on square from above: ", square_of_numbers)
print("************************************")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -11]
min_digit = min(digits)
max_digit = max(digits)
sum_of_all_digits = sum(digits)
print("All digits in the list are", digits)
print("Min digit is", min_digit)
print("Max digit is", max_digit)
print("Sum of all digits in the list is", sum_of_all_digits)
print("************************************")
## List Comprehensions
squares_v2 = [value ** 2 for value in range(1, 11)]
print("Demo for list comprehension", squares_v2)
print("************************************")

# Working with part of a list
argentina_football_players = ["Musso", "Tagliafico", "Martinez", "Romero", "Otamendi", "Palacios", "Fernandez", "Alvarez", "MacAlistar", "Messi"]
print("Squat members of National football team of Argentina :", argentina_football_players)
first_three_players = argentina_football_players[0:3]
print("First three players are", first_three_players)
print("From second to fourth are ", argentina_football_players[1:4])
print("From third to the end: ", argentina_football_players[2:])
print("Last three players are: ", argentina_football_players[-3:])
#Copy the entire list.
afa = argentina_football_players[:]
print(afa)