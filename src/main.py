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

        # for testing through terminal
        # while True:
        #     game.try_place_domino(screen, None)

        clock = pygame.time.Clock()

        # for testing through gui
        game.show_bg(screen)
        while True:
            clock.tick(Const.FPS)
            for event in pygame.event.get():

                # quit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # end of game
                if event.type == Const.END_EVENT:
                    Game.end_of_game(screen)

                # place domino
                if Const.PLAYER_TURN and Const.START:
                    if event.type == pygame.MOUSEBUTTONUP:
                        move_info = Const.read_coords(event.pos)
                        game.try_place_domino(screen, move_info)
                else:
                    if Const.START:
                        game.computer_play(screen)



            pygame.display.update()

main = Main()
if(Const.START):
    main.mainloop()
