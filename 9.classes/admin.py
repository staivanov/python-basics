from user import User
from privileges import Privileges


class Admin(User):
    """ This class represent an Administrator who is special kind of user with full access in the system."""

    def __init__(self, first_name: str, last_name: str, username : str, gender : str, age: int, login_attempts: int, privileges: Privileges):
        super().__init__(first_name, last_name, username, gender, age, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

    def __iter__(self):
        """Allows the Admin instance to be iterable by delegating to its privileges."""
        return iter(self.privileges)

