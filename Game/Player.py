__author__ = "Felix Hubert"

from random import randint


class Player:
    def __init__(self, name, dice_number):
        self.name = name
        self.dice = []
        self.dice_number = dice_number


    def roll(self):
        """
        Rolls all the dice of the player
        :return: void
        """
        self.dice = []
        for i in range(1, self.dice_number + 1):
            n = randint(1, 6)
            self.dice.append(n)

    def lose_round(self):
        """
        Loses 1 die after losing a round
        :return: void
        """
        self.dice_number -= 1

    def get_dice_string(self):
        """
        Returns a string of the dice value the player currently have
        :return: string
        """
        string = ""
        for i, die in enumerate(self.dice):
            if i == self.dice_number - 1:
                string += str(die)
            else:
                string += str(die) + " "
        return string
