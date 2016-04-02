__author__ = "Felix Hubert"

import time

import Player
import Utils


class Game:
    def __init__(self, player_number, start_dice_number):
        self.player_list = []
        self.game_over = False
        self.player_turn = 1
        self.player_number = player_number
        self.generate_players(start_dice_number)

    def play(self):
        while not self.game_over:
            self.prepare_round()
            self.play_round()
        print "#######"
        print "Game over!"
        player = self.player_list[0]
        print "Winner is: " + player.name

    def generate_players(self, start_dice_number):
        for i in range(1, int(self.player_number) + 1):
            name = "Player" + str(i)
            player = Player.Player(name, start_dice_number)
            self.player_list.append(player)

    def prepare_round(self):
        print "#######"
        print "Everyone Roll!"
        for player in self.player_list:
            player.roll()
        print "There are " + str(self.get_dice_number()) + " dice in play"

    def play_round(self):
        print "###############"
        turn_over = False
        previous_bet = [0, 0]
        while not turn_over:
            current_player = self.player_list[self.player_turn - 1]

            print current_player.name + "'s turn to play"

            if current_player.name == "Player1":
                print "Here are your dice:"
                print current_player.get_dice_string()
                print "You need to beat [" + str(previous_bet[0]) + ", " + str(previous_bet[1]) + "]"
                print """
                What do you want to do?
                1. Bet
                2. Bullshit
                """
                choice = int(raw_input())
                while choice != 1 and choice != 2:
                    choice = int(raw_input())

                if choice == 1:
                    previous_bet = self.ask_bet(previous_bet)

                else:
                    turn_over = True

            else:
                print "AI TURN"
                AI_bet = Utils.AI_bet(previous_bet, self.get_dice_number())
                if AI_bet == [-1, -1]:
                    print "AI calls Bullshit"
                    turn_over = True
                else:
                    previous_bet = AI_bet
                    print "AI calls [" + str(previous_bet[0]) + ", " + str(previous_bet[1]) + "]"

                time.sleep(2)

            if not turn_over:
                if self.player_turn >= len(self.player_list):
                    self.player_turn = 1
                else:
                    self.player_turn += 1

        actual_dice_quantity = self.calculate_dice_number(previous_bet[1])
        print "There are " + str(actual_dice_quantity) + " " + str(previous_bet[1]) + " in total"
        time.sleep(2)

        if actual_dice_quantity >= previous_bet[0]:
            print "Current player lose 1 die"
            player = self.player_list[self.player_number - 1]
            player.lose_round()
        else:
            print "Previous player lose 1 die"
            if self.player_turn == 1:
                player = self.player_list[self.player_number - 1]
            else:
                player = self.player_list[self.player_number - 2]
            player.lose_round()

        time.sleep(2)
        self.game_over = self.look_for_dead_player()
        time.sleep(2)

    def ask_bet(self, bet_to_beat):
        valid_bet = False
        bet = []
        while not valid_bet:
            print "____"
            print "Please enter your bet."

            bet_nb = int(raw_input("Number of dice: "))
            bet_value = int(raw_input("Value of die: "))
            bet.insert(0, bet_nb)
            bet.insert(1, bet_value)
            if Utils.verify_bid(bet_to_beat, bet):
                valid_bet = True
            else:
                print "Invalid bet."
        print "______________"
        return bet

    def calculate_dice_number(self, value):
        actual_nb = 0
        for player in self.player_list:
            for die in player.dice:
                if die == value:
                    actual_nb += 1
        return actual_nb

    def look_for_dead_player(self):
        for player in self.player_list:
            if player.dice_number == 0:
                print player.name + " has no die anymore."
                self.player_list.remove(player)

        if len(self.player_list) == 1:
            return True

        print "#########"
        print "Current remaining players are:"
        for player in self.player_list:
            print player.name
        print "#########"

    def get_dice_number(self):
        total = 0
        for player in self.player_list:
            total += player.dice_number
        return total
