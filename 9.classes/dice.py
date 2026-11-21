from random import randint


class Die:
    """ This class represent a die with one attribute sides. """
    MIN_DIE_SIDE: int = 1

    def __init__(self, sides: int = 6) -> None:
        """ Initializer an attribute sides"""
        if sides < 1:
            raise ValueError("A die must have at least one side.")
        self.sides: int = sides

    def roll_die(self) -> None:
        """ This function represents a simulation of rolling a die from 1 to user defined sides. The result is a randomly generated integer number."""
        dice_current_number: int = randint(MIN_DIE_SIDE, self.sides)
        print(dice_current_number)
        return
