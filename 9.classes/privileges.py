class Privileges:
    """ Every instance of this class represents a list of privileges on some admin instance. """
    def __init__(self, list_of_privileges):
        self.list_of_privileges = list_of_privileges

    def show_privileges(self):
        """ Show all privileges one by one in a sequence order. """
        for privilege in self.list_of_privileges:
            print(privilege)

    def  __iter__(self):
        """ Makes the Privileges instance iterable. """
        return iter(self.list_of_privileges)