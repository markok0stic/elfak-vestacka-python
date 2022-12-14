import pygame.image


class Square:

    def __init__(self, row, col, piece=None, domino=None, heuristic=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.domino = domino
        self.heuristic = heuristic 

    def has_place(self):
        return self.piece is None

    def occupy(self, letter):
        self.piece = [letter]

    def has_domino(self):
        return self.domino is not None
