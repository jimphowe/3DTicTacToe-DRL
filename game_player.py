from board import Board
from piece import Piece
from random_agent import RandomAgent

class GamePlayer:
    def __init__(self):
      self.player1 = RandomAgent(Piece.WHITE)
      self.player2 = RandomAgent(Piece.RED)
      self.board = Board()

    def playGame(self):
       while 1 == 1:
          # Player 1 moves
          (x1,y1,z1,dir1) = self.player1.getMove(self.board)
          self.board.move(x1,y1,z1,dir1,Piece.WHITE)
          print(self.board.getGameState())
          if self.board.hasWon(Piece.WHITE):
             print('White wins!')
             return
          # Player 2 moves
          (x2,y2,z2,dir2) = self.player2.getMove(self.board)
          self.board.move(x2,y2,z2,dir2,Piece.RED)
          print(self.board.getGameState())
          if self.board.hasWon(Piece.RED):
             print('Red wins!')
             return