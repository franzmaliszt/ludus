import random
from config import DICE_SIZE


class Dice:
    def __init__(self):
        self.faces = DICE_SIZE
        self.result = 0

    def roll(self):
        self.result = random.randint(1, 20)
