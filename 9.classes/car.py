class Car:
    """Class representing instance of car with his attributes."""

    def __init__(self, make: str, model: str | int, year: int, odometer: int):
        """ Initialize attributes for the current instance of the car. """
        self.make: str = make
        self.model: str | int = model
        self.year: int = year
        self.odometer: int = 0

    def get_description(self) -> str:
        """ Return a neatly formatted descriptive name. """
        car_description: str = f"{self.make} {self.model} from {self.year} year."
        return car_description

    def read_odometer(self) -> int:
        return self.odometer

    def update_odometer(self, km: int) -> None:
        if km >= self.odometer:
            self.odometer = km
        else:
            print("You can't roll back an odometer.")

    def increase_odometer(self, km: int) -> None:

        if km > 0:
            self.odometer += km
        else:
            print("You can't increase the odometer by a negative value.")
