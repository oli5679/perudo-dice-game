__author__ = "Felix Hubert"

from random import randint


class Player:
    def __init__(self, name, dice_number):
        self.name = name
        self.dice = []
        self.dice_number = dice_number

    def roll(self):
        self.dice = []
        for i in range(1, self.dice_number + 1):
            n = randint(1, 6)
            self.dice.append(n)

    def lose_round(self):
        self.dice_number -= 1

    def get_dice_string(self):
        string = ""
        for i, die in enumerate(self.dice):
            if i == self.dice_number - 1:
                string += str(die)
            else:
                string += str(die) + " "
        return string
