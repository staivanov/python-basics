# 5.1 Write series of conditional tests.
car: str = "Porsche"
porsche: str = "Porsche"
print("Is car == Porsche? I predict True")
do_cars_match: bool = car == porsche
print(do_cars_match)

car: str = "BMW"
porsche: str = "Porsche"
print("Is car == Audi? I predict True")
are_porsche_and_car_same: bool = car == porsche
print(are_porsche_and_car_same)

car: str = "Lexus"
toyota: str = "Toyota"
print("Is car == Toyota? I predict True")
are_toyota_and_car_same: bool = car == toyota
print(are_toyota_and_car_same)

car: str = "Acura"
honda: str = "Honda"
print("Is car == Acura? I predict True")
are_honda_and_car_different: bool = not car == honda
print(are_honda_and_car_different)
print("*" * 30)

# 5.3 Alien Colors 1.
blue_color: str = "blue"
alien_color: str = blue_color
green_color: str = "green"
red_color: str = "red"
player_points: int = 0
yellow_color: int = 0

if alien_color == green_color:
    print("Green. You just earn 5 points.")
    player_points: int = 5
elif alien_color == blue_color:
    print("Blue. You just earn 20 points.")
    player_points: int = 20
    print()
elif alien_color == red_color:
    print("Red. You just earn 15 points.")
    player_points: int = 15
    print()
elif alien_color == yellow_color:
    print("Yellow. You just earn 10 points.")
    player_points: int = 10
else:
    player_points: int = 3
    print()

print("*" * 30)

# 5.6 Stages of Life
person_age: int = 36

baby_age: int = 2
toddler_age: int = 4
kid_age: int = 13
teenager_age: int = 20
adult_age: int = 65
elder_age: int = 65

if person_age < baby_age:
    print("You are a baby.")
elif baby_age <= person_age < toddler_age:
    print("You are a toddler.")
elif toddler_age <= person_age < kid_age:
    print("You are a kid.")
elif kid_age <= person_age < teenager_age:
    print("You are a teenager.")
elif teenager_age <= person_age < adult_age:
    print("You are an adult.")
elif elder_age >= person_age:
    print("You are an elder.")

print("*" * 30)

# 5.7 Favorite fruit
banana: str = "banana"
apple: str = "apple"
pineapple: str = "pineapple"
fav_fruits: list[str] = [banana, apple, pineapple]

if "pear" in fav_fruits:
    print("You really like pear!")
if "apricot" in fav_fruits:
    print("You really like apricot!")
if banana in fav_fruits:
    print("You really like", banana, end="!\n", flush=True)
if apple in fav_fruits:
    print("You really like", apple, end="!\n", flush=True)
if pineapple in fav_fruits:
    print("You really like", pineapple, end="!\n", flush=True)
print("*" * 30)

# 5.8 Hello Admin
admin: str = "admin"
users: list[str] = ["dellan", "hall", "Pirata", admin, "kiko"]

for user in users:
    if user == admin:
        print(f"Hello, {admin}, would you like to see a status report?")
    else:
        print(f"Hello, {user}, thank you for logging in again.")
# Check if users list is empty. If it is return `true`. That's why negate logical operator `not` is used.
if not users:
    print("We need to find some users!")

print("*" * 30)

# 5.10 Checking usernames

current_users: list[str] = ["kiril", "antoan", "libristo", "jana", "kalina"]
new_users: list[str] = ["kiril", "kalina", "kepy", "maestro", "otamendi"]
for new_user in current_users:
    if new_user in new_users:
        print("You need to enter a new username, because this is already registered.")
    else:
        print("Your username is free. You can register it.")

print("*" * 30)

# 5.11 Ordinal Numbers
numbers_v2: list[int] = list(range(1, 10))

for number in numbers_v2:
    if number == 1:
        print("1st", end=" ", flush=True)
    elif number == 2:
        print("2nd", end=" ", flush=True)
    elif number == 3:
        print("3rd", end=" ", flush=True)
    else:
        print(f"{number}th", end=" ", flush=True)
