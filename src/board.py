from square import Square
from const import *


def valid_move(move_info):
    res = False
    if Const.PLACE_VERT and ((move_info[0] + 1) <= Const.ROWS - 1) and (
            Const.get_letter_index(move_info[1]) <= Const.COLS - 1):
        res = True
    elif not Const.PLACE_VERT and ((move_info[0]) <= Const.ROWS - 1) and (Const.get_letter_index(move_info[1]) + 1 <= Const.COLS - 1):
        res = True

    return res


class Board:

    def __init__(self):
        self.squares = []
        self._create()

    def _create(self):

        row = []
        for i in range(0, Const.COLS):
            row.append(0)
        for col in range(Const.ROWS):
            self.squares = [row.copy() for col in range(Const.ROWS)]

        for i in range(0, Const.ROWS):
            for j in range(0, Const.COLS):
                self.squares[i][j] = Square(i, Const.ALFABET[j])

        self.print_table()

    def board_has_place(self, move):
        res = False

        # validate move
        if not valid_move(move):
            return res

        # valid move check is free
        if self.squares[move[0]][Const.get_letter_index(move[1])].has_place():
            if Const.PLACE_VERT and self.squares[move[0] + 1][Const.get_letter_index(move[1])].has_place():
                res = True
            elif not Const.PLACE_VERT and self.squares[move[0]][Const.get_letter_index(move[1]) + 1].has_place():
                res = True

        return res

    def occupy_squares(self, move):
        print(move)
        if Const.PLACE_VERT:
            self.squares[move[0]][int(Const.get_letter_index(move[1]))].piece = 'X'
            self.squares[move[0] + 1][int(Const.get_letter_index(move[1]))].piece = 'X'
        else:
            self.squares[move[0]][Const.get_letter_index(move[1])].piece = 'O'
            self.squares[move[0]][Const.get_letter_index(move[1]) + 1].piece = 'O'
        self.print_table()

    def print_table(self):
        for i in range(Const.ROWS - 1, -1, -1):
            z = [(i + 1)]
            for j in self.squares[i]:
                z.append(j.piece)
            print(z)
