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

        if Const.PLACE_VERT:
            color = Const.VCOLOR
            if self.board.squares[row1][col1].has_domino():
                rect = (col1 * Const.SQSIZE + Const.DOMINO_MARGIN, row1 * Const.SQSIZE + Const.DOMINO_MARGIN,
                        Const.SQSIZE - 2 * Const.DOMINO_MARGIN, Const.SQSIZE - Const.DOMINO_MARGIN)
                pygame.draw.rect(surface, color, rect)

            if self.board.squares[row2][col2].has_domino():
                rect = (
                col2 * Const.SQSIZE + Const.DOMINO_MARGIN, row2 * Const.SQSIZE, Const.SQSIZE - 2 * Const.DOMINO_MARGIN,
                Const.SQSIZE - Const.DOMINO_MARGIN)
                pygame.draw.rect(surface, color, rect)
        else:
            color = Const.HCOLOR
            if self.board.squares[row1][col1].has_domino():
                rect = (col1 * Const.SQSIZE + Const.DOMINO_MARGIN, row1 * Const.SQSIZE + Const.DOMINO_MARGIN,
                        Const.SQSIZE - Const.DOMINO_MARGIN, Const.SQSIZE - 2 * Const.DOMINO_MARGIN)
                pygame.draw.rect(surface, color, rect)

            if self.board.squares[row2][col2].has_domino():
                rect = (
                col2 * Const.SQSIZE, row2 * Const.SQSIZE + Const.DOMINO_MARGIN, Const.SQSIZE - Const.DOMINO_MARGIN,
                Const.SQSIZE - 2 * Const.DOMINO_MARGIN)
                pygame.draw.rect(surface, color, rect)

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

        if not self.has_more_moves():
            pygame.event.post(pygame.event.Event(Const.END_EVENT))
            print("End")

    def has_more_moves(self):
        for row in range(0, Const.ROWS):
            for col in range(0, Const.COLS):
                if self.board.board_has_place((row, Const.get_letter(col))):
                    return True
        return False

    def end_of_game(screen):
        if Const.PLACE_VERT:
            text = Const.WINNER_FONT.render("Black Wins!", 1, Const.WHITE_COLOR)
        else:
            text = Const.WINNER_FONT.render("Orange Wins!", 1, Const.WHITE_COLOR)

        frame = ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2 - 7),
                 (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2 - 7), text.get_width() + 14,
                 text.get_height() + 14)
        canvas = ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2),
                  (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2), text.get_width(), text.get_height())

        pygame.draw.rect(screen, (212, 175, 55), frame)
        pygame.draw.rect(screen, (119, 154, 88), canvas)
        screen.blit(text, ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2),
                           (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2)))
