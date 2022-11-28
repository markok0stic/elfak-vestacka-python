from square import Square
from const import *
class Board:

    def __init__(self):
        self.squares = []

    def _create(self):
        row = []
        for i in range(0,ROWS):
            row.append(0)
        self.squares = [row for col in range(COLS)]

        print(self.squares)
        for i in range(ROWS):
            for j in range(COLS):
                self.squares[i][j] = Square(i,j)

b = Board()
b._create()