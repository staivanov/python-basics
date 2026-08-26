from car import Car
from battery import Battery

class ElectricCar(Car):
    """ Represent an electric car. """

    def __init__(self, make, model, year, odometer, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year, odometer)
        self.Battery = Battery(battery_size)

    def get_description(self):
        """ Return a neatly formatted descriptive name for current instance of Electric car. """
        car_description = f"{self.make} {self.model} with {self.Battery.size} kW from {self.year} year."
        return car_description