# 6.1 Person
person = {}
person["first_name"] = "Stanislav"
person["last_name"] = "Ivanov"
person["age"] = 36
person["country"] = "Bulgaria"

for current_data in person:
    print(person[current_data])

print("****************************")
# 6.2 Favorite numbers.
people_fav_numbers = {
    "Tom": 5,
    "Alexis": 12,
    "Nicole": 2,
    "Cory": 99,
    "Julia": 6
}
print("****************************")
# 6.3 Glossary
glossary = {
    "[]": "Empty brackets creat an empty list.",
    "print()": "In Python, you use the built-in print() function to display output to the console.",
    "range(start, stop, step)": "The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.",
    "tuple": "Tuple items are ordered, indexed, unchangeable, and allow duplicate values.",
    "max()": "This function returns biggest value in the list."
}

for keyword, meaning in glossary.items():
    print(keyword)
    print(f"\t{meaning}")
print("**************************************")
# 6.5 Rivers
rivers = {
    "Dunav": ["Germany", "Austria", "Slovakia", "Hungary", "Croatia", "Serbia", "Romania", "Bulgaria", "Moldova",
              "Ukraine"],
    "Nile": ["Burundi", "the Democratic Republic of the Congo", "Egypt", "Eritrea", "Ethiopia", "Kenya", "Rwanda",
             "South Sudan", "Sudan", "Tanzania", "Ugand"],
    "Ural": ["Russia", "Kazakhstan"]
}

for river, countries in rivers.items():
    print(f"The river {river} runs through {countries}")

# Print all keys
for river in rivers.keys():
    print(river)

# Print all values. Every country for every current river.
for river, countries in rivers.items():
    print(countries)

print("**************************************")
# 6.6 Polling
students_with_favorite_languages = {
    "Stanislav": ["C++", "C", "Java", "Python", ],
    "Ivan": ["php", "JavaScript", ],
    "Yoana": ["JavaScript", "Java", ],
    "Petar": ["C#", "Java"]
}

students_who_should_take_the_poll = ["Ivan", "Yoana", "Alexandra", "Kendra", "Neno"]
students_with_favorite_languages_keys = students_with_favorite_languages.keys()

for student in students_who_should_take_the_poll:
    if student in students_with_favorite_languages_keys:
        print(f"Thanks for responding, {student}")
    else:
        print(f"Please, take the poll, {student}")

print("**************************************")
# 6.7 People
person_1 = {
    "first_name": "Yoana",
    "last_name": "Vasileva",
    "age": 27,
    "country": "Bulgaria",
}
person_2 = {
    "first_name": "Atanas",
    "last_name": "Kalimitis",
    "age": 32,
    "country": "Greece",
}
person_3 = {
    "first_name": "Jonas",
    "last_name": "Reagan",
    "age": 24,
    "country": "USA",
}

people = [person, person_1, person_2, person_3]

for current_person in people:
    person_full_name = f"{current_person["first_name"]} {current_person["last_name"]}"
    print(f"{person_full_name}, {current_person["age"]} years old, is from {current_person["country"]}")

print("**************************************")
# 6.8 Pets
dog = {
    "kind of animal": "domesticated mammal",
    "owner": "Stanislav",
    "age": 5,
    "name": "Darth Maul"

}

cat = {
    "kind of animal": "domesticated carnivorous mammal",
    "owner": "Maria",
    "age": 8,
    "name": "Count Dooku"
}

hamster = {
    "kind of animal": "small mammal",
    "owner": "Valeri",
    "age": 2,
    "name": "Fifi"
}

chicken = {
    "kind of animal": "domesticated bird",
    "owner": "Lili",
    "age": 10,
    "name": "Petya"
}

cock = {
    "kind of animal": "domesticated male chicken",
    "owner": "Petko",
    "age": 4,
    "name": "Petko"
}

pets = [dog, cat, hamster, chicken, cock]

for pet in pets:
    print(pet)

print("**************************************")
# 6.9 Favorite Places:
favorite_places = {
    "Stanislav": {
        "K2": "The second-highest mountain on Earth, after Mount Everest at 8,849 metres (29,032 ft).[3] It lies in the Karakoram range.",
        "Copacabana": "It is most prominently known for its 4 km (2.5 mile) balneario beach, which is one of the most famous in the world.",
        "Machu Picchu": "Among the greatest artistic, architectural and land use achievements anywhere and the most significant tangible legacy of the Inca civilization."},
    "Natalie": {
        "Golden Sands": "Major seaside resort town on the northern Bulgarian Black Sea Coast, adjacent to a national park of the same name in the municipality of Varna.",
        "Rila National Park": "Largest national park in Bulgaria spanning an area of 810.46 km2 in the Rila mountain range in the south-west of the country.",
    },
    "Yoni": {
        "Versailles": " a château and historic monument in Versailles in the Yvelines department of France, southwest of Paris.",
        "Kruger National Park, South Africa": "Where nearly 2 million hectares of unrivaled diversity of life forms fuses"
                                              " with historical and archaeological sights – this is real Africa."
                                              " The world-renowned Kruger National Park offers a wildlife experience that ranks with the best in Africa."
    }
}

print("**************************************")
# 6.10 Favorite Numbers
ppl_fav_numbers = {
    "Tom": [5, 7, 22, 99],
    "Alexis": [12, 1, 79, 4],
    "Nicole": [1, 2, 3],
    "Cory": [66, 85, 666],
    "Julia": [6, 69, 24]
}

for person, fav_numbers in ppl_fav_numbers.items():
    print(person)
    print(f"\tFavorite numbers are: {fav_numbers}")

print("**************************************")
# 6.11 Cities

cities = {
    "Varna": {
        "country": "Bulgaria",
        "population": 322682,
        "km sq": 238,
        "fact": "Sea capital of Bulgaria"
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14270000,
        "km sq": 2194,
        "fact": "Capital of Japan"
    },
    "Washington D.C.": {
        "population": 8176300,
        "km sq": 177.0,
        "fact": "Capital of USA"
    }
}

for city, description in cities.items():
    print(city)
    for section in description:
        print(f"\t{section} - {description[section]}")
