# 1. Start with an empty dictionary
from typing import KeysView, ValuesView

car_0: set[()] = {}

# 2. Adding items.
car_0["brand"]: str = "Porsche"
car_0["model"]: str = "Panamera"
car_0["engine_type"]: str = "Petrol - Twin Turbo"
car_0["kW"]: int = 600
car_0["color"]: str = "black"

# 3. Print every key-value pair in the dictionary.
for spec in car_0:
    print(f"{spec}: {car_0[spec]}")
print("*" * 30)

# 4. Remocing key-value pari
del car_0["color"]

# 5. It's an error if I try to access not existing element in a dictionary.
# print(car_0["coupe_type]"). Method .get() is an easy solution for this problem.
coupe_type: str = car_0.get("coupe_type", "There is not suck key.")
print(coupe_type)
print("*" * 30)
# 6. Another way to iterate through a dictionary.

for key, value in car_0.items():
    print(f"key: \t{key}")
    print(f"value: \t{value}")

print("*" * 30)

# 7. Get all keys of dictionary. Loop through them.
car_0_keys: KeysView[str] = car_0.keys()

for current_key in car_0_keys:
    print(f"{current_key} is the current key of car_0")

print("*" * 30)

# 8. Get all keys of a dictionary. Sort them and loop through them.

people_fav_numbers: dict[str, int] = {
    "Tom": 5,
    "Alexis": 12,
    "Nicole": 2,
    "Cory": 99,
    "Julia": 6
}

names_sorted = sorted(people_fav_numbers.keys())

for current_name in names_sorted:
    print(f"Hi, it's {current_name}!")

print("*" * 30)

# 9. Get all values even that repeats from a dictionary.
all_numbers: ValuesView[int] = people_fav_numbers.values()

for number in all_numbers:
    print(number)

print("*" * 30)
# 10. Get all unique values from a dictionary.
people_guessed_number: dict[str, int] = {
    "Alex": 22,
    "Clara": 15,
    "Tom": 15,
    "Lisa": 22,
    "Cindy": 1,
    "Johny": 8,
    "Stanislav": 9,
    "Eli": 5,
    "Moni": 8,
}

all_unique_numbers: set[int] = set(people_guessed_number.values())
print("All unique numbers are:")

for number in all_unique_numbers:
    print(number)

print("*" * 30)

# 11. Set
programming_languages: set[str] = {"C++", "C", "Java", "Python", "JavaScript", }

# 12. Nesting
car_1: dict[str, str | int] = {"brand": "BMW", "model": "760", "engine_type": "twin-turbo V12", "kW": 480,
                               "color": "white", }
car_2: dict[str, str | int] = {"brand": "BMW", "model": "M5", "engine_type": "twin-turbo v8", "kW": 400,
                               "color": "red", }
car_3: dict[str, str | int] = {"brand": "BMW", "model": 325, "engine_type": "4-cylinder diesel", "kW": 120,
                               "color": "blue", }

cars: list[dict] = [car_0, car_1, car_2, car_3]
print("Those are the first two cars on my list of cars.")

for car in cars[:2]:
    print(car)

print("*" * 30)

# 13. List in a Dictionary
students_with_favorite_languages: dict[str, list[str]] = {
    "Stanislav": ["C++", "C", "Python", ],
    "Ivan": ["php", "JavaScript", ],
    "Yoana": ["JavaScript", "Java", ],
    "Petar": ["C#", "Java"]
}

for student, programming_languages in students_with_favorite_languages.items():
    print(f"{student}")
    for language in programming_languages:
        print(f"\t{language}")
