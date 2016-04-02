__author__ = 'Felix Hubert'

from Game import Game

import unittest

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game.Game(6, 6)

    def test_player_generation_names(self):
        self.assertEqual("Player5", self.game.player_list[4])
        self.assertEqual("Player1", self.game.player_list[0])
        self.assertEqual(6, len(self.game.player_list))

    def test_init_players_dice_numer(self):
        player = self.game.player_list[3]
        self.assertEqual(6, player.dice_number)

    #TODO more game tests