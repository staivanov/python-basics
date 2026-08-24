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
        car_description = f"{self.make} {self.model} {self.year}"
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
