class User:

    def __init__(self, first_name, last_name, username, gender, age):
        """Initialize a new user with his first name, last name, username, gender and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.age = age

    def describe_user(self):
        """ A function that prints on the console all attributes with their values about the current instance of the user. """
        print(f" First name: {self.first_name}\n Last name: {self.last_name}\n Username: {self.username}\n Gender: {self.gender}\n Age: {self.age}\n")

    def greet_user(self):
        """ A simple greeting message for the current instance on user"""
        print(f"Hola, {self.username}!")