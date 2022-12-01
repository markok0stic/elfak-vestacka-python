from square import Square
from const import *


def valid_move(move_info):
    res = False

    if Const.PLACE_VERT and ((move_info[0] + 1) <= Const.ROWS) and (Const.get_letter_index(move_info[1]) <= Const.COLS):
        res = True
    elif not Const.PLACE_VERT and ((move_info[0]) <= Const.ROWS) and (Const.get_letter_index(move_info[1]) + 1 > Const.COLS):
        res = True

    return res


class Board:

    def __init__(self):
        self.squares = []
        self._create()

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
        res = False

        # validate move
        if not valid_move(move):
            return res

        # valid move check is free
        if self.squares[move[0]][Const.get_letter_index(move[1])].has_place():
            if Const.PLACE_VERT and self.squares[move[0]][Const.get_letter_index(move[1]) + 1].has_place():
                res = True
            elif not Const.PLACE_VERT and self.squares[move[0] + 1][Const.get_letter_index(move[1])].has_place():
                res = True

        return res

    def occupy_squares(self, move):
        if Const.PLACE_VERT:
            self.squares[move[0]][int(Const.get_letter_index(move[1]))].piece = 'X'
            self.squares[move[0]][int(Const.get_letter_index(move[1]) + 1)].piece = 'X'
            print((f'Postavljena domina na pozicijama: ({0},{1}) | ({0},{2})').format(move[0], move[1],
                                                                                      Const.get_next_letter(move[1])))
        else:
            self.squares[move[0]][Const.get_letter_index(move[1])].piece = 'O'
            self.squares[move[0]][Const.get_letter_index(move[1]) + 1].piece = 'O'
            print((f'Postavljena domina na pozicijama: ({1},{0}) | ({2},{0})').format(move[1], move[0], move[0] + 1))
