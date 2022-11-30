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
                self.squares[i][j] = Square(i, Const.ALFABET[j])

    def has_place(self, move):
        move_info = list(move)
        move_info[0] = int(move_info[0])

        # validate move
        if not self.valid_move(move_info):
            return

        # valid move check is free
        if self.squares[move_info[0]][Const.get_letter_index(move_info[1])].has_place():
            if Const.PLACE_VERT and self.squares[move_info[0]][Const.get_letter_index(move_info[1]) + 1].has_place():
                print('postavi ver')
                Const.PLACE_VERT = not Const.PLACE_VERT
            elif not Const.PLACE_VERT and self.squares[move_info[0] + 1][
                Const.get_letter_index(move_info[1])].has_place():
                print('postvi hor')
                Const.PLACE_VERT = not Const.PLACE_VERT
            else:
                print('Nema')
        else:
            print('Nema')

    def valid_move(self, move_info):
        if (move_info[0] + 1) > Const.ROWS or Const.get_letter_index(move_info[1]) + 1 > Const.COLS:
            return False
        return True
