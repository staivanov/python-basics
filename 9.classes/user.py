class User:

    def __init__(self, first_name, last_name, username, gender, age, login_attempts=0):
        """Initialize a new user with his first name, last name, username, gender, age and login attempts."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        """ A function that prints on the console all attributes with their values about the current instance of the user. """
        print(
            f" First name: {self.first_name}\n Last name: {self.last_name}\n Username: {self.username}\n Gender: {self.gender}\n Age: {self.age}\n")

    def greet_user(self):
        """ A simple greeting message for the current instance on user"""
        print(f"Hola, {self.username}!")

    def increment_login_attempts(self):
        """ This function increments with one logging attempts to the current user."""
        self.login_attempts += 1

    def reset_logging_attempts(self):
        """ This function reset logging attempts to the current user."""
        self.login_attempts = 0
