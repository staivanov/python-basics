class Battery:
    """ A simple battery for an electrical car. """

    def __init__(self, size):
        """ Initializer battery with user-defined size. """
        self.size = size

    def describe_battery(self):
        """ This method provides info about the battery size to the current Electric car instance."""
        battery_description = f"This car has a {self.size}-kWh battery."
        return battery_description
