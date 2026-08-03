#8.1 Message
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
make_shirt(size = "M", text_message = "Bangaranga")

def make_shirt(size = "M", text_message = "I am using Python."):
    message = f"On your T-shirt have a text \"{text_message}\". size: {size}."
    print(message)

make_shirt()
make_shirt(size="L")
make_shirt("XXL", "Java is cool!")