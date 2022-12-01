import pygame
import sys

from const import *
from game import Game
from form import GameForm
from board import Board

class Main:
    def __init__(self):
        self.screen = None
        self.game = None
        self.board = None
        GameForm()

    def mainloop(self):
        self.screen = pygame.display.set_mode((Const.COLS * Const.SQSIZE, Const.ROWS * Const.SQSIZE))
        self.game = Game()
        pygame.init()
        pygame.display.set_caption('Domineering')

        game = self.game
        screen = self.screen
        while True:
            game.show_bg(screen)

            for event in pygame.event.get():

                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # place domino
                if event.type == pygame.MOUSEBUTTONUP:
                    self.game.try_place_domino()

            pygame.display.update()


main = Main()
main.mainloop()