# Simple function  def without parameters.
def greeting_to_the_world():
    """Print a simple message."""
    message = "No no, no no no no, no no no no, no no there's no limit!!!"
    print(message)


greeting_to_the_world()
print("***********************************************")


# Simple function def with parameters.

def calc_rectangle_area(length, width):
    """This function calculate the area of a rectangle """
    return length * width


a = 5
b = 10
res = calc_rectangle_area(a, b)
print("The area of your rectangle is ", res, "cm.")
print("***********************************************")


# Positional Arguments
def describe_car(brand, model):
    """Display information about a car and the model."""
    print(f"{brand} {model}")


brand = "Porsche"
model = "911 RS2"
describe_car(brand, model)

brand_v2 = "Ford"
model = "F-150 Raptor"
describe_car(brand_v2, model)

print("***********************************************")

# Keyword Arguments
describe_car(brand="BMW", model="M8")


# Default values
def describe_car(model, brand="BMW"):
    """Display information about a car and the model."""
    print(f"{brand} {model}")


describe_car("335i")
describe_car("Land Cruiser", brand="Toyota")

print("***********************************************")


# A function with an optional argument.

def get_full_name_formatted(first_name, last_name, middle_name=""):
    """Return a full name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        first_and_last_name = f"{first_name} {last_name}"
        return first_and_last_name.title()


full_name_without_middle = get_full_name_formatted("Stanislav", "Ivanov")
print(full_name_without_middle)
full_name = get_full_name_formatted("Linus", "Benedict", "Torvalds")
print(full_name)


# Returning a Dictionary

def build_person(first_name, last_name, gender, nationality, age=None, ):
    """Build a new person with a provided information."""
    person = {
        "first": first_name,
        "last": last_name,
        "gender": gender,
        "nationality": nationality
    }
    if age:
        person["age"] = age

    return person


current_bulgarian_primer_minister = build_person("Rumen", "Radev", "male", 63, "bulgarian")
print(f"The current prime minster on the Republic of Bulgaria is \n\t {current_bulgarian_primer_minister}.")

