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
        """
        Will start the game and run until a winner his found
        :return: void
        """
        while not self.game_over:
            self.prepare_round()
            self.play_round()
        print "#######"
        print "Game over!"
        player = self.player_list[0]
        print "Winner is: " + player.name

    def generate_players(self, start_dice_number):
        """
        Will generate the players based on the user input and will
        give them dice based on the user input. Will give them name
        based on the number they are generated (Player1, Player2, Player3, etc)
        :param start_dice_number:
        :return: void
        """
        for i in range(1, int(self.player_number) + 1):
            name = "Player" + str(i)
            player = Player.Player(name, start_dice_number)
            self.player_list.append(player)

    def prepare_round(self):
        """
        Will make everyone roll their dice and show the number of total
        dice for the round
        :return: void
        """
        print "#######"
        print "Everyone Roll!"
        for player in self.player_list:
            player.roll()
        print "There are " + str(self.get_dice_number()) + " dice in play"

    def play_round(self):
        """
        Will play a round of Perudo.
        If the current player is Player1, it will ask for user input.
        Otherwise, it will simulate an AI response to play with the user.

        Will trigger end of game if at the end of the round everybody have no die except 1 player.
        The round is over when the first player calls bullshit. It will then calculate the winner of
        the round and try to find for dead players.
        :return:
        """
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
        """
        Will ask the user input for a bet
        :param bet_to_beat:
        :return: bet
        """
        valid_bet = False
        bet = []
        while not valid_bet:
            print "____"
            print "Please enter your bet."

            bet_nb = int(raw_input("Number of dice: "))
            bet_value = int(raw_input("Value of die: "))
            bet.insert(0, bet_nb)
            bet.insert(1, bet_value)
            if Utils.verify_bet(bet_to_beat, bet):
                valid_bet = True
            else:
                print "Invalid bet."
        print "______________"
        return bet

    def calculate_dice_number(self, value):
        """
        Will verify the number of dice of a certain value in the dice of all players.
        :param value:
        :return: dice_number
        """
        actual_nb = 0
        for player in self.player_list:
            for die in player.dice:
                if die == value:
                    actual_nb += 1
        return actual_nb

    def look_for_dead_player(self):
        """
        Will verify if a player is dead and will remove it from the player list.
        :return:
        """
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
        """
        Calculates the total number of dice available in the game
        :return:
        """
        total = 0
        for player in self.player_list:
            total += player.dice_number
        return total
