# Simple function  def without parameters.
def greeting_to_the_world():
    """Print a simple message."""
    message = "No no, no no no no, no no no no, no no there's no limit!!!"
    print(message)

greeting_to_the_world()
print("***********************************************")

#Simple function def with parameters.

def calcRectangleArea(length, width):
    """This function calculate the area of a rectangle """
    return  length * width

a = 5
b = 10
res = calcRectangleArea(a, b)
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
describe_car(brand = "BMW", model = "M8")


# Default values
def describe_car(model, brand = "BMW"):
    """Display information about a car and the model."""
    print(f"{brand} {model}")

describe_car("335i")
describe_car("Land Cruiser", brand = "Toyota")

