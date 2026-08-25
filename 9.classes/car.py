class Car:
    """Class representing instance of car with his attributes."""

    def __init__(self, make, model, year, odometer):
        """ Initialize attributes for the current instance of the car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        """ Return a neatly formatted descriptive name. """
        car_description = f"{self.make} {self.model} from {self.year} year."
        return car_description

    def read_odometer(self):
        return self.odometer

    def update_odometer(self, km):
        self.odometer = km
        if km >= self.odometer:
            odometer = km
        else:
            print(" You can't roll back an odometer.")

    def increase_odometer(self, km):
        self.odometer += km

class ElectricCar(Car):
    """ Represent an electric car. """
    def __init__(self, make, model, year, odometer, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year, odometer)
        self.battery_size = battery_size

    def get_description(self):
        """ Return a neatly formatted descriptive name for current instance of Electric car. """
        car_description = f"{self.make} {self.model} with {self.battery_size} kW from {self.year} year."
        return car_description

    def describe_battery(self):
        """ This method provides info about the battery size to the current Electric car instance."""
        battery_description = f"This car has a {self.battery_size}-kWh battery."
        return battery_description