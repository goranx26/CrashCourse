from random import randint


class Die():
    """Creates a dice class"""
    def __init__(self, sides=6):
        """Inits the dice with optional number of sides"""
        self.sides = sides

    def roll_die(self, rolls):
        """Rolls the die/dice"""
        while True:
            print(randint(1, self.sides))
            rolls -= 1
            if rolls == 0:
                break


nr_sides = input('How many sides you want on that die?')
my_dice = Die(int(nr_sides))
nr_rolls = input('How many rolls?')
my_dice.roll_die(int(nr_rolls))



