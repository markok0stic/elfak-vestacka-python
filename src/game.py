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
        self.v_domino = Domino((255, 255, 255), 1.0, -1, (2, 1))
        self.h_domino = Domino((0, 0, 0), 1.0, 1, (1, 2))

    def show_bg(self, surface):
        for row in range(Const.ROWS):
            for col in range(Const.COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * Const.SQSIZE, row * Const.SQSIZE, Const.SQSIZE, Const.SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_domino(self, surface, direction):
        if direction == Const.HDIR:

            for row in range(Const.ROWS):
                for col in range(Const.COLS):
                    if self.board.squares[row][col].has_place():
                        piece = self.board.squares[row][col].piece

    def try_place_domino(self):
        move_info = read_inputs()
        if self.board.board_has_place(move_info):
            self.board.occupy_squares(move_info)
            # self.show_domino(move_info)
            # switch_player()
        else:
            print('No room for that move!')
