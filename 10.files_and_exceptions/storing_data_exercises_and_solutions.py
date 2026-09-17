import json
from pathlib import Path


#  10.11-10.12 Favorite number.

# filename = 'favorite-number.json'
# path = Path(filename)
#
# if path.exists():
#     fav_user_number_serialized = path.read_text()
#     fav_user_number = json.loads(fav_user_number_serialized)
#     print(fav_user_number)
# else:
#     fav_number = int(input("What is your favorite number? "))
#     fav_number_serialized = json.dumps(fav_number)
#     path.write_text(fav_number_serialized)

#  10.13 User Dictionary.


def make_user() -> dict:
    """ This function make a new user.

Args:
   None.

Returns:
    A new user with appropriate attributes in a dictionary.
"""
    username = input("What is your username? ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    gender = input("What is your gender? ")
    age = int(input("What is your age? "))
    new_user = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age
    }
    return new_user


def get_stored_user(path: Path) -> dict | None:
    """ Return a user in a dictionary type from a provided Path. """
    if path.exists():
        user_contents = path.read_text()
        stored_user = json.loads(user_contents)
        return stored_user
    else:
        return None


def store_user(user: dict) -> None:
    """ Store a user. """
    path_name = f"{user.get('username')}.json"
    path = Path(path_name)
    user_serialized = json.dumps(user)
    path.write_text(user_serialized)


def print_user_summary(user: dict):
    """ Print a summary for the provided user. """
    summary = f"The user with the nickname {user.get('username')} has the name {user.get('first_name')} {user.get('last_name')}. It\'s a {user.get('gender')} on {user.get('age')} years old."
    print(summary)


current_user = make_user()
store_user(current_user)
current_user_path_name = f"{current_user.get('username')}.json"
current_user_path = Path(current_user_path_name)
user = get_stored_user(current_user_path)
print_user_summary(user)
