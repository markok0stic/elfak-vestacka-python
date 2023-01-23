import pygame
from const import *
from board import Board
from domino import *
import random


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
    Const.PLAYER_TURN = not Const.PLAYER_TURN 

def save_context():
    return(Const.PLACE_VERT, Const.PLAYER_TURN)

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
            if self.board.squares[row1][col1].has_domino() and self.board.squares[row2][col2].has_domino():
                self.board.draw_vertical_domino(col1, row1, col2, row2, surface, Const.VCOLOR)

        else:
            if self.board.squares[row1][col1].has_domino() and self.board.squares[row2][col2].has_domino():
                self.board.draw_horizontal_domino(col1, row1, col2, row2, surface, Const.HCOLOR)

    def try_place_domino(self, screen, inputs=None):
        move_info = inputs

        if inputs is None:
            move_info = read_inputs()

        if self.board.board_has_place(move_info):
            square_coords = self.board.occupy_squares(move_info)
            self.show_domino(screen, square_coords)
            if Const.PLACE_VERT:
                Const.VPUT_SOUND.play()
            else:
                Const.HPUT_SOUND.play() 
            switch_player()
            print('Possible moves:')
            print(self.possible_moves(self.board))
            print('\n')
        else:
            print('No room for that move!')
            print('\n') 

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
        if Const.PLAYER_TURN:
            text = Const.WINNER_FONT.render("YOU LOST!", 1, Const.WHITE_COLOR)
            Const.LOSE_SOUND.play()
        else:
            text = Const.WINNER_FONT.render("YOU WON!", 1, Const.WHITE_COLOR)
            Const.WIN_SOUND.play()

        frame = ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2 - 7),
                 (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2 - 7), text.get_width() + 14,
                 text.get_height() + 14)
        canvas = ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2),
                  (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2), text.get_width(), text.get_height())

        pygame.draw.rect(screen, (212, 175, 55), frame)
        pygame.draw.rect(screen, (119, 154, 88), canvas)
        screen.blit(text, ((Const.COLS * Const.SQSIZE // 2 - text.get_width() // 2), (Const.ROWS * Const.SQSIZE // 2 - text.get_height() // 2)))

        Const.START = False

    def possible_moves(self, board):
        response = []
        for row in range(0, Const.ROWS):
            for col in range(0, Const.COLS):
                if board.board_has_place((row, Const.get_letter(col))):
                    response.append((row, col))

        return response

    def opponent_possible_moves(self, board):    
        switch_player()
        response = self.possible_moves(board)
        switch_player()
        return response

    def new_state(self, move, board_state, player): # kreira novo stanje 
        Const.PLACE_VERT = player
        new_state = Board()
        new_state.copy_board(board_state)
        new_state.occupy_squares((move[0], Const.get_letter(move[1])))
        switch_player()

        return new_state

    def evaluate_state(self, board_state):
        response = 0
        my_moves = self.opponent_possible_moves(board_state)
        opponent_moves = self.possible_moves(board_state)
        response = len(opponent_moves) - len(my_moves)

        return response
    
    def min_best_move(self, board_state, depth, alpha, beta, next_move = None):
        list_of_moves = self.possible_moves(board_state)
        if depth == 0 or list_of_moves is None or len(list_of_moves) == 0:
            return (next_move, self.evaluate_state(board_state))
        else:
            for move in list_of_moves:
                beta = min(beta, self.max_best_move(self.new_state(move, board_state, Const.COMPUTER_FIGURE), depth-1, alpha, beta,
                 move if next_move is None else next_move), key = lambda x: x[1])
                if beta[1] <= alpha[1]:
                    return alpha
        return beta

    def max_best_move(self, board_state, depth, alpha, beta, next_move = None):
        list_of_moves = self.possible_moves(board_state)
        if depth == 0 or list_of_moves is None or len(list_of_moves) == 0:
            return (next_move, self.evaluate_state(board_state))
        else:
            for move in list_of_moves:
                alpha = max(alpha, self.min_best_move(self.new_state(move, board_state, not Const.COMPUTER_FIGURE), depth-1, alpha, beta,
                 move if next_move is None else next_move), key = lambda x: x[1])
                if alpha[1] >= beta[1]:
                    return beta
        return alpha

    def minmax_best_move(self, board_state, depth, alpha=(None, -Const.INFINITIVE), beta=(None, Const.INFINITIVE)):
        if Const.PLAYER_TURN:
            return self.max_best_move(board_state, depth, alpha, beta)
        else:
            return self.min_best_move(board_state, depth, alpha, beta)

    def computer_play(self, screen):
        if Const.ROWS>5 and Const.COLS>5 and Const.MOVE_NUMBER<4:
            Const.MOVE_NUMBER += 1
            if Const.PLACE_VERT:
                ind=random.randint(0,Const.END)
                move=Const.VERTICAL_PLAYER_MOVES.pop(ind)
                Const.END -= 1
                while not self.board.board_has_place((move[0], Const.get_letter(move[1]))):
                    ind=random.randint(0,Const.END)
                    move=Const.VERTICAL_PLAYER_MOVES.pop(ind)
                    Const.END -= 1
            else:
                ind=random.randint(0,Const.END)
                move=Const.HORIZONTAL_PLAYER_MOVES.pop(ind)
                Const.END -= 1
                while not self.board.board_has_place((move[0], Const.get_letter(move[1]))):
                    ind=random.randint(0,Const.END)
                    move=Const.HORIZONTAL_PLAYER_MOVES.pop(ind)
                    Const.END -= 1               
            square_coords=self.board.occupy_squares((move[0], Const.get_letter(move[1])))
            self.show_domino(screen, square_coords)
        else:
            context = save_context()
            Const.COMPUTER_FIGURE = Const.PLACE_VERT
            move = self.minmax_best_move(self.board, 3)
            Const.PLACE_VERT = context[0]
            Const.PLAYER_TURN = context[1]

            square_coords = self.board.occupy_squares((move[0][0], Const.get_letter(move[0][1])))
            self.show_domino(screen, square_coords)
        
        if Const.PLACE_VERT:
            Const.VPUT_SOUND.play()
        else:
            Const.HPUT_SOUND.play()  
        
        switch_player()
        
        if not self.has_more_moves():
            pygame.event.post(pygame.event.Event(Const.END_EVENT))
            print("End")
     
