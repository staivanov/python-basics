# 8.1 Message
def display_message():
    """This function displays what I am learning right now."""
    print("I am learning how functions work in Python.")


display_message()
print("******************************************")


# 8.2 Favorite Book
def favorite_book(title):
    """This function prints message with your favorite book on the console."""
    print(f"One of my favorite books is {title.title()}.")


my_book = "Shogun"
favorite_book(my_book)
print("******************************************")


# 8.3 T-Shirt
def make_shirt(size, text_message):
    message = f"On your T-shirt have a text \"{text_message}\". size: {size}."
    print(message)


make_shirt("S", "Offline till I drink my coffee")
make_shirt(size="M", text_message="Bangaranga")


def make_shirt(size="M", text_message="I am using Python."):
    message = f"On your T-shirt have a text \"{text_message}\". size: {size}."
    print(message)


make_shirt()
make_shirt(size="L")
make_shirt("XXL", "Java is cool!")
print("******************************************")


# 8.5 Cities
def describe_city(city_name, country_name="Bulgaria"):
    """This function print a simple sentence with your provided city and country."""
    print(f"{city_name} is in {country_name}.")


describe_city("Varna")
describe_city(city_name="Plovdiv")
describe_city(city_name="Barcelona", country_name="Spain")
print("******************************************")


# 8.6 City Names
def city_country(city, country):
    location = f"{city}, {country}"
    return location


plovdiv = city_country("Plovdiv", "Bulgaria")
print(plovdiv)
buenos_aires = city_country("Buenos Aires", "Argentina")
print(buenos_aires)
panama = city_country("Panama", "Panama")
print(panama)
print("******************************************")


# 8.7 Album
def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        "artist": artist_name,
        "album_title": album_title,
    }
    if number_of_songs:
        album["songs_number"] = number_of_songs
    return album


# n1. album
run_dmc = "RUN-D.M.C"
run_dmc_best_album_name = "King of Rock"
run_dmc_best_album = make_album(run_dmc, run_dmc_best_album_name)
print(run_dmc_best_album)
# n2. album
motley_crue = "Mötley Crüe"
motley_crue_best_album_name = "Dr. Feelgood"
motley_crue_best_album = make_album(motley_crue, motley_crue_best_album_name)
print(motley_crue_best_album)
# n3. album
deep_purple = "Deep Purple"
dp_latest_album_name = "SPLAT!"
songs_number = 13
deep_purple_latest_album = make_album(deep_purple, dp_latest_album_name, songs_number)
print(deep_purple_latest_album)
print("******************************************")

# 8.8 User Album
quit = "q"

# while True:
#
#     artist = input("Please, enter name of the artist. Enter \'q\' for quit.\n")
#
#     if artist == quit: break
#
#     name_of_the_album = input("Please, enter name of the album.\n")
#     number_of_songs = 0
#
#     try:
#         number_of_songs = int(input("How many song are in the album.\n"))
#     except:
#         print("Invalid input!")
#
#     if number_of_songs > 0:
#         current_album = make_album(artist, name_of_the_album, number_of_songs)
#     else:
#        current_album = make_album(artist, name_of_the_album)
#
#     print(f"{current_album} \n")

# 8.9 Messages
text_messages = ["Hello, reader!", "Good mooring, mthfkrs", "Girls, girls, girls!",
                 "You wake up late for school, man, you don't wanna go"]


def show_messages(text_messages):
    for message in text_messages:
        print(message)


show_messages(text_messages)
print("******************************************")


# 8.10 Sending Messages

def send_messages(messages, sent_messages):
    while messages:
        current_msg = messages.pop()
        print(current_msg)
        sent_messages.append(current_msg)


sent_messages = []
send_messages(text_messages, sent_messages)

# 8.11 Archived Messages.
text_messages_v2 = ["Hello, reader!", "Good mooring, mthfkrs", "Girls, girls, girls!",
                    "You wake up late for school, man, you don't wanna go"]
sent_messages_v2 = []
send_messages(text_messages_v2[:], sent_messages_v2)
# After function invocation content in text_messages is preserved, because this version use a copy of the list text_messages_v2.
print(sent_messages_v2)
print(text_messages_v2)
print("******************************************")


# 8.12 Sandwiches
def make_sandwich(sandwich_name, *items):
    print(f"Your sandwich `{sandwich_name}` has these ingredients: ")
    for item in items[0]:
        print(f"\t{item}")


greek_sandwich_ingredients = ["soft pita", "feta cheese", "ripe tomatoes", "cucumbers", "red onions", "Kalamata olives"]
make_sandwich("Greek sandwich", greek_sandwich_ingredients)
princess_ingredients = ["minced meat", "bread slices"]
make_sandwich("princess", princess_ingredients)
baked_spicy_chicken_ingredients = ["breadcrumbs", "garlic powder", "smoked paprika", "cayenne", "salt", "pepper",
                                   "skinless chicken breast"]
make_sandwich("Baked spicy chicken", baked_spicy_chicken_ingredients)
print("******************************************")


# 8.13 User profile
def build_profile(first_name, last_name, **description):
    description["first_name"] = first_name
    description["last_name"] = last_name
    return description


bio = build_profile("Stanislav", "Ivanov", gender="male",
                    age=36, nationality="bulgarian", job="The Best In The World!")
print(bio)
print("******************************************")

# 8.14 Cars
def make_car(manufacturer, model, **description):
    description["manufacturer"] = manufacturer
    description["model"] = model
    return description

monster_car = make_car("Ford", "Focus", engine_power_Hp = 101, engine_type = "diesel", doors = 5)
for k,v in monster_car.items():
    print(f"{k} - {v}")