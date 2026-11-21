class Battery:
    """ A simple battery for an electrical car. """

    def __init__(self, size: int) -> None:
        """ Initializer battery with user-defined size. """
        self.size: int = size

    def describe_battery(self) -> str:
        """ This method provides info about the battery size to the current Electric car instance."""
        battery_description: str = f"This car has a {self.size}-kWh battery."
        return battery_description
