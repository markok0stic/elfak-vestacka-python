class Const:
    WIDTH = 750
    HEIGHT = 750

    HDIR = -10
    VDIR = -11

    ROWS = 10
    COLS = 10
    FIRST_PLAYER = 0

    PLACE_VERT = True

    ALFABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V',
               'W', 'X', 'Y', 'Z']

    SQSIZE = WIDTH // COLS

    def get_next_letter(letter):
        return Const.ALFABET[Const.ALFABET.index(letter) + 1]

    def get_letter_index(letter):
        return Const.ALFABET.index(letter)

    def read_coords(pos):
        x, y = pos
        return [y // Const.SQSIZE - (1 if Const.PLACE_VERT else 0), Const.ALFABET[x // Const.SQSIZE]]


staticmethod(Const.get_next_letter)
staticmethod(Const.get_letter_index)
