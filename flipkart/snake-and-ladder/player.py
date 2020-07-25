class Player(object):
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def roll_dice(self, board, dice):
        dice_total = dice.roll_dice()
        current_pos = self.pos
        if (dice_total + self.pos) <= 100:
            self.pos += dice_total
        if self.pos in board.snakes:
            self.pos = board.snakes[self.pos]
        if self.pos in board.ladders:
            self.pos = board.ladders[self.pos]
        print(str(self.name)+" moved from "+str(current_pos)+" to "+str(self.pos))
        return self.pos
