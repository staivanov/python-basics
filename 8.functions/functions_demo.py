# Simple function  def without parameters.
def greeting_to_the_world():
    """Print a simple message."""
    message = "Evil never comes alone!"
    print(message)
    message = "Fighting the world!"
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
print("The are of your rectangle is ", res)
print("***********************************************")

