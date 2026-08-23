class Restaurant:
    """Represent a restaurant class with his name and cuisine food type."""
    def __init__(self, name, cuisine_type):
        """ Initialize name and cuisine type for the current instance. """
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ A simple function that prints all information about the restaurant current instance. """
        print(f"Restaurant name is {self.name} with {self.cuisine_type} food.")

    def open_restaurant(self):
        """ A simple function that prints a welcome message to all on the console. """
        print(f"Welcome to {self.name}!")