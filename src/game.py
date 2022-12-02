import pygame
from const import *
from board import Board
from domino import Domino


def read_inputs():
    move_info = input()
    move_info = move_info.replace('[', '')
    move_info = move_info.replace(']', '')
    move_info = move_info.replace(',', '')
    move_info = move_info.replace(' ', '')

    letter = move_info[-1]
    move_info = move_info.replace(move_info[-1], '')
    move = [int(move_info), letter]

    if move[0] > 0:
        move[0] -= 1

    return move


def switch_player():
    Const.PLACE_VERT = not Const.PLACE_VERT


class Game:

    def __init__(self):
        self.board = Board()

    def show_bg(self, surface):
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * Const.SQSIZE, row * Const.SQSIZE, Const.SQSIZE, Const.SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_domino(self, surface, square_coords):

        row1 = square_coords[0][0]
        col1 = square_coords[0][1]

        row2 = square_coords[1][0]
        col2 = square_coords[1][1]

        if self.board.squares[row1][col1].has_domino():
            rect = (col1 * Const.SQSIZE, row1 * Const.SQSIZE, Const.SQSIZE, Const.SQSIZE)
            pygame.draw.rect(surface, (233, 123, 55), rect)

        if self.board.squares[row2][col2].has_domino():
            rect = (col2 * Const.SQSIZE, row2 * Const.SQSIZE, Const.SQSIZE, Const.SQSIZE)
            pygame.draw.rect(surface, (233, 123, 55), rect)

    def try_place_domino(self, screen, inputs=None):
        move_info = inputs

        if inputs is None:
            move_info = read_inputs()

        if self.board.board_has_place(move_info):
            square_coords = self.board.occupy_squares(move_info)
            self.show_domino(screen, square_coords)
            switch_player()
        else:
            print('No room for that move!')
