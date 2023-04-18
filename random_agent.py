from board import Board
import random

directions = ['UP','DOWN','LEFT','RIGHT','FRONT','BACK']

class RandomAgent:
    def __init__(self,player):
        self.player = player

    def getMove(self, board: Board):
        x = random.randint(0,2)
        y = random.randint(0,2)
        z = random.randint(0,2)
        dir = random.choice(directions)
        while not board.validMove(x,y,z,dir):
            x = random.randint(0,2)
            y = random.randint(0,2)
            z = random.randint(0,2)
            dir = random.choice(directions)
        return (x,y,z,dir)