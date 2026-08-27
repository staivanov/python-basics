from random import randint


class Die:
    """ This class represent a die with one attribute sides. """

    def __init__(self, sides: int = 6):
        """ Initializer an attribute sides"""
        self.sides = sides

    def roll_die(self):
        """ This function represents a simulation of rolling a die from 1 to user defined sides. The result is a randomly generated integer number."""
        dice_current_number = randint(1, self.sides)
        print(dice_current_number)
        return
