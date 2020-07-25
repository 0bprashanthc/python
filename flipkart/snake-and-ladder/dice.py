import random

class Dice(object):
    def __init__(self, dice_count):
        self.dice_count = dice_count
        self.dice_start = 1
        self.dice_end = 6

    def roll_dice(self):
        roll_total = 0
        for dice in range(self.dice_count):
            roll_total += random.randint(self.dice_start, self.dice_end)
        return roll_total
