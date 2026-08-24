class Restaurant:
    """Represent a restaurant class with his name and cuisine food type."""

    def __init__(self, name, cuisine_type, number_served=0):
        """ Initialize name and cuisine type for the current instance. """
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """ A simple function that prints all information about the restaurant current instance. """
        print(f"Restaurant name is {self.name} with {self.cuisine_type} food.")

    def open_restaurant(self):
        """ A simple function that prints a welcome message to all on the console. """
        print(f"Welcome to {self.name}!")

    def set_number_served(self, portions):
        """ This function set the number of served portions at the current restaurant instance."""
        self.number_served = portions

    def increment_number_served(self, portions_to_add):
        """ This function add user defined number of served portions to the current served portions on the restaurant instance."""
        self.number_served += portions_to_add
