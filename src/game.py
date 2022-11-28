import pygame
from const import *
from board import Board
from domino import Domino
class Game:

    def __init__(self):
        self.board = Board()
        self.v_domino = Domino((255,255,255),1.0,-1,(2,1))
        self.h_domino = Domino((0,0,0),1.0,1,(1,2))

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_domino(self, surface, direction):
        if direction == HDIR:

            for row in range(ROWS):
                for col in range(COLS):
                    if self.board.squares[row][col].has_place():
                        piece = self.board.squares[row][col].piece
    pass


