from piece import Piece

class Board:
    def __init__(self):
        self.pieces = [[[Piece.EMPTY for k in range(3)] for j in range(3)] for i in range(3)]
        self.winningRuns = self.getWinningRuns()

    def validMove(self,x,y,z,dir):
        if not x in range(3) or not y in range(3) or not z in range(3):
              return False
        match dir:
              case 'UP':
                    return (z == 2) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x][y][z-1] == Piece.EMPTY or self.pieces[x][y][z-2] == Piece.EMPTY)
              case 'DOWN':
                    return (z == 0) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x][y][z+1] == Piece.EMPTY or self.pieces[x][y][z+2] == Piece.EMPTY)
              case 'LEFT':
                    return (x == 2) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x-1][y][z] == Piece.EMPTY or self.pieces[x-2][y][z] == Piece.EMPTY)
              case 'RIGHT':
                    return (x == 0) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x+1][y][z] == Piece.EMPTY or self.pieces[x+2][y][z] == Piece.EMPTY)
              case 'FRONT':
                    return (y == 2) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x][y-1][z] == Piece.EMPTY or self.pieces[x][y-2][z] == Piece.EMPTY)
              case 'BACK':
                    return (y == 0) and (self.pieces[x][y][z] == Piece.EMPTY or self.pieces[x][y+1][z] == Piece.EMPTY or self.pieces[x][y+2][z] == Piece.EMPTY)
              case _:
                  return False
            
    def move(self,x,y,z,dir,player: Piece):
        if not self.validMove(x,y,z,dir):
             raise ValueError
        else:
             if (self.pieces[x][y][z] == Piece.EMPTY):
                  self.pieces[x][y][z] = player
             else:
                match dir:
                    case 'UP':
                       if (self.pieces[x][y][z-1] == Piece.EMPTY):
                         self.pieces[x][y][z-1] = self.pieces[x][y][z]
                         self.pieces[x][y][z] = player
                       else:
                         self.pieces[x][y][z-2] = self.pieces[x][y][z-1]
                         self.pieces[x][y][z-1] = self.pieces[x][y][z]
                         self.pieces[x][y][z] = player
                    case 'DOWN':
                        if (self.pieces[x][y][z+1] == Piece.EMPTY):
                          self.pieces[x][y][z+1] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                        else:
                          self.pieces[x][y][z+2] = self.pieces[x][y][z+1]
                          self.pieces[x][y][z+1] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                    case 'LEFT':
                        if (self.pieces[x-1][y][z] == Piece.EMPTY):
                          self.pieces[x-1][y][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                        else:
                          self.pieces[x-2][y][z] = self.pieces[x-1][y][z]
                          self.pieces[x-1][y][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                    case 'RIGHT':
                        if (self.pieces[x+1][y][z] == Piece.EMPTY):
                          self.pieces[x+1][y][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                        else:
                          self.pieces[x+2][y][z] = self.pieces[x+1][y][z]
                          self.pieces[x+1][y][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                    case 'FRONT':
                        if (self.pieces[x][y-1][z] == Piece.EMPTY):
                          self.pieces[x][y-1][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                        else:
                          self.pieces[x][y-2][z] = self.pieces[x][y-1][z]
                          self.pieces[x][y-1][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                    case 'BACK':
                        if (self.pieces[x][y+1][z] == Piece.EMPTY):
                          self.pieces[x][y+1][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player
                        else:
                          self.pieces[x][y+2][z] = self.pieces[x][y+1][z]
                          self.pieces[x][y+1][z] = self.pieces[x][y][z]
                          self.pieces[x][y][z] = player

    def getGameState(self):
        gameState = "+----------------------\n"
        gameState += "| \ " + self.pieces[0][2][0].value + "  " + self.pieces[1][2][0].value + "  " + self.pieces[2][2][0].value + " \\\n"
        gameState += "|   \                     \\\n"
        gameState += "|     \ " + self.pieces[0][1][0].value + "  " + self.pieces[1][1][0].value + "  " + self.pieces[2][1][0].value + " \\\n"
        gameState += "|       \                     \\\n"
        gameState += "|         \ " + self.pieces[0][0][0].value + "  " + self.pieces[1][0][0].value + "  " + self.pieces[2][0][0].value + " \\\n"
        gameState += "|          ---------------------|\n"
        gameState += "|   " + self.pieces[0][2][1].value + " |" + self.pieces[1][2][1].value + "  " + self.pieces[2][2][1].value + "         |\n"
        gameState += "|         |                     |\n"
        gameState += "|       " + self.pieces[0][1][1].value + "  " + self.pieces[1][1][1].value + "  " + self.pieces[2][1][1].value + "     |\n"
        gameState += "|         |                     |\n"
        gameState += "|         | " + self.pieces[0][0][1].value + "  " + self.pieces[1][0][1].value + "  " + self.pieces[2][0][1].value + " |\n"
        gameState += "|         |                     |\n"
        gameState += " \ " + self.pieces[0][2][2].value + "  " + self.pieces[1][2][2].value + "  " + self.pieces[2][2][2].value + "          |\n"
        gameState += "   \      |                     |\n"
        gameState += "     \ " + self.pieces[0][1][2].value + "  " + self.pieces[1][1][2].value + "  " + self.pieces[2][1][2].value + "      |\n"
        gameState += "       \  |                     |\n"
        gameState += "         \| " + self.pieces[0][0][2].value + "  " + self.pieces[1][0][2].value + "  " + self.pieces[2][0][2].value + " |\n"
        gameState += "           ---------------------+\n\n"
        return gameState
    

    def getWinningRuns(self):
        runs = []

        runs.append([(0,0,0),(0,0,1),(0,0,2)])
        runs.append([(0,0,0),(0,1,0),(0,2,0)])
        runs.append([(0,0,0),(1,0,0),(2,0,0)])

        runs.append([(2,2,0),(1,2,0),(0,2,0)])
        runs.append([(2,2,0),(2,1,0),(2,0,0)])
        runs.append([(2,2,0),(2,2,1),(2,2,2)])

        runs.append([(0,2,2),(0,1,2),(0,0,2)])
        runs.append([(0,2,2),(1,2,2),(2,2,2)])
        runs.append([(0,2,2),(0,2,1),(0,2,0)])

        runs.append([(2,0,2),(2,0,1),(2,0,0)])
        runs.append([(2,0,2),(1,0,2),(0,0,2)])
        runs.append([(2,0,2),(2,1,2),(2,2,2)])
        # Front
        runs.append([(0,0,0),(1,0,1),(2,0,2)])
        runs.append([(0,0,2),(1,0,1),(2,0,0)])
        runs.append([(1,0,0),(1,0,1),(1,0,2)])
        runs.append([(0,0,1),(1,0,1),(2,0,1)])
        # Top
        runs.append([(0,0,0),(1,1,0),(2,2,0)])
        runs.append([(0,2,0),(1,1,0),(2,0,0)])
        runs.append([(0,1,0),(1,1,0),(2,1,0)])
        runs.append([(1,2,0),(1,1,0),(1,0,0)])
        # Left
        runs.append([(0,0,0),(0,1,1),(0,2,2)])
        runs.append([(0,0,2),(0,1,1),(0,2,0)])
        runs.append([(0,0,1),(0,1,1),(0,2,1)])
        runs.append([(0,1,0),(0,1,1),(0,1,2)])
        # Back
        runs.append([(0,2,2),(1,2,1),(2,2,0)])
        runs.append([(0,2,0),(1,2,1),(2,2,2)])
        runs.append([(1,2,0),(1,2,1),(1,2,2)])
        runs.append([(0,2,1),(1,2,1),(2,2,1)])
        # Right
        runs.append([(2,0,2),(2,1,1),(2,2,0)])
        runs.append([(2,0,0),(2,1,1),(2,2,2)])
        runs.append([(2,0,1),(2,1,1),(2,2,1)])
        runs.append([(2,1,0),(2,1,1),(2,1,2)])
        # Bottom
        runs.append([(2,0,2),(1,1,2),(0,2,2)])
        runs.append([(0,0,2),(1,1,2),(2,2,2)])
        runs.append([(0,1,2),(1,1,2),(2,1,2)])
        runs.append([(1,0,2),(1,1,2),(1,2,2)])
        # Corners
        runs.append([(0,0,0),(1,1,1),(2,2,2)])
        runs.append([(2,0,0),(1,1,1),(0,2,2)])
        runs.append([(2,2,0),(1,1,1),(0,0,2)])
        runs.append([(0,2,0),(1,1,1),(2,0,2)])
        # Edges
        runs.append([(1,0,0),(1,1,1),(1,2,2)])
        runs.append([(2,1,0),(1,1,1),(0,1,2)])
        runs.append([(1,2,0),(1,1,1),(1,0,2)])
        runs.append([(0,1,0),(1,1,1),(2,1,2)])
        runs.append([(0,0,1),(1,1,1),(2,2,1)])
        runs.append([(2,0,1),(1,1,1),(0,2,1)])
        # Middles
        runs.append([(1,1,0),(1,1,1),(1,1,2)])
        runs.append([(1,0,1),(1,1,1),(1,2,1)])
        runs.append([(0,1,1),(1,1,1),(2,1,1)])

        return runs

    def hasWon(self,player: Piece):
        for run in self.winningRuns:
            if all(self.pieces[x][y][z] == player for (x,y,z) in run):
                return True
        return False
    
    def gameOver(self):
        return self.hasWon(Piece.RED) or self.hasWon(Piece.WHITE)
