from pathlib import Path
import json


def get_stored_username(path):
    """ Get stored username if it is available."""
    if path.exists():
        username_contents = path.read_text()
        username = json.loads(username_contents)
        return username
    else:
        return None


def get_new_username(path):
    """ Prompt for a new username. """
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """ Greet the user by name. """
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"You are saved, {username}.")


greet_user()
