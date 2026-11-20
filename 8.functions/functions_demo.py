# Simple function  def without parameters.
def greeting_to_the_world() -> None:
    """Print a simple message."""
    message: str = "No no, no no no no, no no no no, no no there's no limit!!!"
    print(message)


greeting_to_the_world()
print("*" * 30)


# Simple function def with parameters.

def calc_rectangle_area(length: int, width: int) -> int:
    """This function calculate the area of a rectangle """
    return length * width


a: int = 5
b: int = 10
rectangle_area: int = calc_rectangle_area(a, b)
rectangle_area_msg: str = f"The area of your rectangle is {rectangle_area} cm."
print(rectangle_area_msg)
print("*" * 30)


# Positional Arguments
def describe_car(brand: str, model: str) -> None:
    """Display information about a car and the model."""
    print(f"{brand} {model}")


brand: str = "Porsche"
model: str = "911 RS2"
describe_car(brand, model)

brand_v2: str = "Ford"
model: str = "F-150 Raptor"
describe_car(brand_v2, model)

print("*" * 30)

# Keyword Arguments
describe_car(brand="BMW", model="M8")


# Default values
def describe_car(model: str, brand: str = "BMW") -> None:
    """Display information about a car and the model."""
    print(f"{brand} {model}")


describe_car("335i")
describe_car("Land Cruiser", brand="Toyota")

print("*" * 30)


# A function with an optional argument.

def get_full_name_formatted(first_name: str, last_name: str, middle_name: str | None = None) -> str:
    """Return a full name."""
    if middle_name:
        current_full_name: str = f"{first_name} {middle_name} {last_name}"
        return current_full_name.title()
    else:
        first_and_last_name: str = f"{first_name} {last_name}"
        return first_and_last_name.title()


full_name_without_middle: str = get_full_name_formatted("Stanislav", "Ivanov")
print(full_name_without_middle)
full_name: str = get_full_name_formatted("Linus", "Benedict", "Torvalds")
print(full_name)


# Returning a Dictionary

def build_person(first_name: str, last_name: str, gender: str, nationality: str, age: int | None = None) -> dict[
    str, str | int]:
    """Build a new person with a provided information."""
    person: dict[str, str | int] = {
        "first": first_name,
        "last": last_name,
        "gender": gender,
        "nationality": nationality
    }
    if age is not None:
        person["age"] = age

    return person


current_bulgarian_primer_minister: dict[str, str | int] = build_person("Rumen", "Radev", "male", "bulgarian", 63)
print(f"The current prime minster on the Republic of Bulgaria is \n\t {current_bulgarian_primer_minister}.")
print("*" * 30)


# Passing a List as a function argument.

def print_all_usernames(users: list[str]) -> None:
    """Print sequentially every username from the provided list."""
    for user in users:
        print(user)


usernames: list[str] = ["ace", "ICEMAN", "MaX_PoweR", "EyeS", "dreben", "bigBasss", "animimi"]
print_all_usernames(usernames)
print("*" * 30)


# Modifying a List in a Function.

def make_all_usernames_lowercase(usernames: list[str]) -> None:
    """ Make every provided username lowercase. """
    index: int = 0
    usernames_length: int = len(usernames)

    while index < usernames_length:
        usernames[index] = usernames[index].lower()
        index += 1


make_all_usernames_lowercase(usernames)
print(usernames)
print("*" * 30)


# Passing an arbitrary number of arguments.

def print_all_colors(*colors: str) -> None:
    """ Print all provided colors to the console. """
    print(colors)


colors: list[str] = ["blue", "red", "white", "black", "yellow"]
print_all_colors(colors)
colors_v2: list[str] = ["purple", "green"]
print_all_colors(colors_v2)
print("*" * 30)


# Mixing positional and arbitrary arguments.
def make_fake_car(brand: str, model: str | int, *parts: str) -> dict[str, str | int | tuple[str, ...]]:
    """ This function make a fake demo car. """
    print(f"{brand} {model}")
    car: dict[str, str | int | tuple[str, ...]] = {
        "brand": brand,
        "model": model,
        "parts": parts
    }
    return car


bulgar_car: dict[str, str | int | tuple[str, ...]] = make_fake_car("Opel", "Corsa", "suspensions", "coupe", "tires",
                                                                   "windows", "stereo",
                                                                   "air conditioner")
print(bulgar_car)
print("*" * 30)


# Using arbitrary keyword arguments.
def build_user_profile(username: str, first_name: str, last_name: str, email: str, **user_info: object) -> dict[
    str, str | object]:
    """Build a dictionary containing everything we know about a user. """
    user_info["username"] = username
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    user_info["email"] = email
    return user_info


user_info: dict[str, object] = {}

user_profile: dict[str, str | object] = build_user_profile("code213", "Alexis",
                                                           "Michael", email="alexael@yahoo.com",
                                                           country="USA", age=28, gender="male")
print(user_profile)
