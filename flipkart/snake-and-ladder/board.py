class Board(object):
    def __init__(self, size, snakes, ladders):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    def is_winner(self, player):
        if player.pos == self.size:
            print(str(player.name)+" is the winner!!")
            return True
        return False
