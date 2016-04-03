__author__ = 'Felix Hubert'

from Game import Utils

import unittest

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_verify_bid_1(self):
        bid1 = [0, 0]
        bid2 = [2, 3]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_2(self):
        bid1 = [2, 3]
        bid2 = [3, 3]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_3(self):
        bid1 = [3, 3]
        bid2 = [3, 4]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_4(self):
        bid1 = [3, 4]
        bid2 = [3, 4]
        self.assertFalse(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_5(self):
        bid1 = [3, 4]
        bid2 = [3, 1]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_6(self):
        bid1 = [3, 1]
        bid2 = [4, 3]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_7(self):
        bid1 = [10, 2]
        bid2 = [10, 1]
        self.assertTrue(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_8(self):
        bid1 = [10, 1]
        bid2 = [1, 3]
        self.assertFalse(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_9(self):
        bid1 = [2, 1]
        bid2 = [1, 1]
        self.assertFalse(Utils.verify_bet(bid1, bid2))

    def test_verify_bid_10(self):
        bid1 = [2, 1]
        bid2 = [2, 2]
        self.assertFalse(Utils.verify_bet(bid1, bid2))

    def test_AI_bet_up_quantity(self):
        dice_number = 36
        last_bet = [4, 1]
        ai_bet = Utils.AI_bet(last_bet, dice_number)
        self.assertTrue(Utils.verify_bet(last_bet, ai_bet))

    def test_AI_bet_up_value(self):
        dice_number = 36
        last_bet = [5, 2]
        ai_bet = Utils.AI_bet(last_bet, dice_number)
        self.assertTrue(Utils.verify_bet(last_bet, ai_bet))

    def test_AI_bet_up_value_perudo(self):
        dice_number = 36
        last_bet = [6, 6]
        ai_bet = Utils.AI_bet(last_bet, dice_number)
        self.assertTrue(Utils.verify_bet(last_bet, ai_bet))

    def test_AI_bet_call_lie(self):
        dice_number = 36
        last_bet = [7, 1]
        ai_bet = Utils.AI_bet(last_bet, dice_number)
        self.assertTrue(Utils.verify_bet(last_bet, ai_bet))

    def test_AI_bet_call_lie_decimal(self):
        dice_number = 32
        last_bet = [5, 1]
        ai_bet = Utils.AI_bet(last_bet, dice_number)
        self.assertTrue(Utils.verify_bet(last_bet, ai_bet))