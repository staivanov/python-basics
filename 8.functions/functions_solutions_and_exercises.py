# 8.1 Message
from typing import Any


def display_message() -> None:
    """This function displays what I am learning right now."""
    msg_or_functions: str = f"I am learning how functions work in Python."
    print(msg_or_functions)


display_message()
print("*" * 30)


# 8.2 Favorite Book
def favorite_book(title: str) -> None:
    """This function prints message with your favorite book on the console."""
    fav_book_msg: str = f"One of my favorite books is {title.title()}."
    print(fav_book_msg)


my_book: str = "Shogun"
favorite_book(my_book)
print("*" * 30)


# 8.3 T-Shirt
def make_shirt(size: str, text_message: str) -> None:
    message: str = f"On your T-shirt have a text \"{text_message}\". size: {size}."
    print(message)


make_shirt("S", "Offline till I drink my coffee")
make_shirt(size="M", text_message="Bangaranga")


def make_shirt(size: str = "M", text_message: str = "I am using Python.") -> None:
    message: str = f"On your T-shirt have a text \"{text_message}\". size: {size}."
    print(message)


make_shirt()
make_shirt(size="L")
make_shirt("XXL", "Java is cool!")
print("*" * 30)


# 8.5 Cities
def describe_city(city_name: str, country_name: str = "Bulgaria") -> None:
    """This function print a simple sentence with your provided city and country."""
    described_city_msg: str = f"{city_name} is in {country_name}."
    print(described_city_msg)


describe_city("Varna")
describe_city(city_name="Plovdiv")
describe_city(city_name="Barcelona", country_name="Spain")
print("*" * 30)


# 8.6 City Names
def city_country(city: str, country: str) -> str:
    location: str = f"{city}, {country}"
    return location


plovdiv: str = city_country("Plovdiv", "Bulgaria")
print(plovdiv)
buenos_aires: str = city_country("Buenos Aires", "Argentina")
print(buenos_aires)
panama: str = city_country("Panama", "Panama")
print(panama)
print("*" * 30)


# 8.7 Album
def make_album(artist_name: str, album_title: str, number_of_songs: int | None = None) -> dict[str, str, int]:
    album: dict[str, str | int] = {
        "artist": artist_name,
        "album_title": album_title,
    }

    if number_of_songs is not None:
        album["songs_number"] = number_of_songs
    return album


# n1. album
run_dmc: str = "RUN-D.M.C"
run_dmc_best_album_name: str = "King of Rock"
run_dmc_best_album: dict[str, str | None] = make_album(run_dmc, run_dmc_best_album_name)
print(run_dmc_best_album)
# n2. album
motley_crue: str = "Mötley Crue"
motley_crue_best_album_name: str = "Dr. Feelgood"
motley_crue_best_album: dict[str, str | None] = make_album(motley_crue, motley_crue_best_album_name)
print(motley_crue_best_album)
# n3. album
deep_purple: str = "Deep Purple"
dp_latest_album_name: str = "SPLAT!"
songs_number: int = 13
deep_purple_latest_album: dict[str, str | None] = make_album(deep_purple, dp_latest_album_name, songs_number)
print(deep_purple_latest_album)
print("*" * 30)

# 8.8 User Album
quit: str = "q"

# while True:
#
#     artist: str = input("Please, enter name of the artist. Enter \'q\' for quit.\n")
#
#     if artist == quit: break
#
#     name_of_the_album: str = input("Please, enter name of the album.\n")
#     number_of_songs: int = 0
#
#     try:
#         number_of_songs: int = int(input("How many song are in the album.\n"))
#     except:
#         print("Invalid input!")
#     any_songs: bool = number_of_songs > 0

#     if any_songs:
#         current_album: dict[str, str | None]   = make_album(artist, name_of_the_album, number_of_songs)
#     else:
#        current_album: dict[str, str | None]   = make_album(artist, name_of_the_album)
#
#     print(f"{current_album} \n")

# 8.9 Messages
text_messages: list[str] = ["Hello, reader!", "Good mooring, mthfkrs", "Girls, girls, girls!",
                            "You wake up late for school, man, you don't wanna go"]


def show_messages(text_messages: list[str]) -> None:
    for message in text_messages:
        print(message)


show_messages(text_messages)
print("*" * 30)


# 8.10 Sending Messages

def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    while messages:
        current_msg: str = messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)


sent_messages: list[str] = []
send_messages(text_messages, sent_messages)

# 8.11 Archived Messages.
text_messages_v2: list[str] = ["Hello, reader!", "Good mooring, mthfkrs", "Girls, girls, girls!",
                               "You wake up late for school, man, you don't wanna go"]
sent_messages_v2: list[str] = []
send_messages(text_messages_v2[:], sent_messages_v2)
# After function invocation content in text_messages is preserved, because this version use a copy of the list text_messages_v2.
print(sent_messages_v2)
print(text_messages_v2)
print("*" * 30)


# 8.12 Sandwiches
def make_sandwich(sandwich_name: str, *items: list[str]) -> None:
    print(f"Your sandwich `{sandwich_name}` has these ingredients: ")
    for item in items[0]:
        print(f"\t{item}")


greek_sandwich_ingredients: list[str] = ["soft pita", "feta cheese", "ripe tomatoes", "cucumbers", "red onions",
                                         "Kalamata olives"]
make_sandwich("Greek sandwich", greek_sandwich_ingredients)
princess_ingredients: list[str] = ["minced meat", "bread slices"]
make_sandwich("princess", princess_ingredients)
baked_spicy_chicken_ingredients: list[str] = ["breadcrumbs", "garlic powder", "smoked paprika", "cayenne", "salt",
                                              "pepper",
                                              "skinless chicken breast"]
make_sandwich("Baked spicy chicken", baked_spicy_chicken_ingredients)
print("*" * 30)


# 8.13 User profile
def build_profile(first_name: str, last_name: str, **description: Any) -> dict[str, Any]:
    description["first_name"]: str = first_name
    description["last_name"]: str = last_name
    return description


bio: dict[str, Any] = build_profile("Stanislav", "Ivanov", gender="male",
                                    age=36, nationality="bulgarian", job="The Best In The World!")
print(bio)
print("*" * 30)


# 8.14 Cars
def make_car(manufacturer: str, model: str, **description: Any) -> dict[str, Any]:
    description["manufacturer"]: str = manufacturer
    description["model"]: str = model
    return description


monster_car: dict[str, Any] = make_car("Ford", "Focus", engine_power_Hp=101, engine_type="diesel", doors=5)

for k, v in monster_car.items():
    print(f"{k} - {v}")
