from dice import Dice
from board import Board
from player import Player

DICE_COUNT = 1
BOARD_SIZE = 100
snakes, ladders, players = dict(), dict(), list()

if __name__ == "__main__":
    with open("input.txt","r") as f:
        snakes_count = int(f.readline())
        for i in range(snakes_count):
            start, end = str(f.readline()).split(' ')
            snakes[start] = end
        ladders_count = int(f.readline())
        for i in range(ladders_count):
            start, end = str(f.readline()).split(' ')
            ladders[start] = end
        players_count = int(f.readline())
        for i in range(players_count):
            player_name = str(f.readline()).strip()
            players.append(Player(player_name))

    dice = Dice(DICE_COUNT)
    board = Board(BOARD_SIZE, snakes, ladders)
    game_to_proceed = True
    while game_to_proceed:
        for each_player in players:
            each_player.roll_dice(board, dice)
            if board.is_winner(each_player):
                game_to_proceed = False
                break
