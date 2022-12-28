from pygame import font
from pygame import USEREVENT
font.init()

class Const:
    WIDTH = 750
    HEIGHT = 750
    WINNER_FONT = font.SysFont('comicsans', 40)
    FPS = 60
    INFINITIVE = 9999
    START = False

    HDIR = -10
    VDIR = -11

    WHITE_COLOR = (255, 255, 255)
    VCOLOR = (233, 123, 55)
    HCOLOR = (0, 0, 0)
    DOMINO_MARGIN = 7

    END_EVENT = USEREVENT + 1

    ROWS = 10
    COLS = 10
    PLAYER_TURN = 0

    PLACE_VERT = True

    #VERTICAL_PLAYER_MOVES =
    #HORIZONTAL_PLAYER_MOVES =

    ALFABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    SQSIZE = WIDTH // COLS

    def get_next_letter(letter):
        return Const.ALFABET[Const.ALFABET.index(letter) + 1]

    def get_letter_index(letter):
        return Const.ALFABET.index(letter)

    def get_letter(index):
        return Const.ALFABET[index]

    def read_coords(pos):
        x, y = pos
        return [y // Const.SQSIZE - (1 if Const.PLACE_VERT else 0), Const.ALFABET[x // Const.SQSIZE]]
    

staticmethod(Const.get_next_letter)
staticmethod(Const.get_letter_index)
