class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_place(self):
        return self.piece is None

    def occupy(self, letter):
        self.piece = [letter]
