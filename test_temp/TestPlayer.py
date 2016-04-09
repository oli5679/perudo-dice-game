__author__ = 'Felix Hubert'

from game import Player

import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player.Player("Player", 6)

    def test_roll(self):
        self.player.roll()
        for die in self.player.dice:
            if die > 6 or die < 0:
                self.fail()

    def test_get_dice_string(self):
        self.player.dice = [3, 1, 5, 4, 5, 6]
        self.assertEqual("3 1 5 4 5 6", self.player.get_dice_string())

    def test_lose_round(self):
        self.player.lose_round()
        self.player.lose_round()
        self.assertEqual(4, self.player.dice_number)