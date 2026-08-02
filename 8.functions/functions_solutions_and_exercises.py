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