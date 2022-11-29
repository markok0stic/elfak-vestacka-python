from square import Square
from const import *


class Board:

    def __init__(self):
        self.squares = []

    def _create(self):
        print(Const.ROWS)
        print(Const.COLS)
        row = []
        for i in range(0, Const.COLS):
            row.append(0)
        self.squares = [row for col in range(Const.ROWS)]

        print(self.squares)
        for i in range(0, Const.ROWS - 2):
            print(self.squares[i])
            for j in range(0, Const.COLS - 2):
                self.squares[i][j] = Square(i, j)

