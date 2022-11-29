import pygame
from const import *
from board import Board
from domino import Domino

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
