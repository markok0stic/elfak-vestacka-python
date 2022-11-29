from square import Square
from const import *
class Board:

    def __init__(self):
        self.squares = []

    def _create(self):
        row = []
        for i in range(0, Const.ROWS):
            row.append(0)
        self.squares = [row for col in range(0, Const.COLS)]

        print(self.squares)
        for i in range(0,Const.ROWS):
            for j in range(0,Const.COLS):
                self.squares[i][j] = Square(i,j)
