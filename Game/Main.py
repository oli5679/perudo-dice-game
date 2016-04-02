__author__ = "Felix Hubert"

from Game import Game

def main():
    player_number = int(raw_input("Enter the number of players: "))
    start_dice_number = int(raw_input("Enter the number of starting die per player: "))
    game = Game(player_number, start_dice_number)
    game.play()

if __name__ == '__main__':
    main()
