from functools import partial
from tkinter import *
from const import *
from tkinter import ttk
import tkinter
from const import *


class GameForm:

    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root, padding=20)
        frm.grid()
        root.title("Domineering")
        rows = tkinter.IntVar()
        cols = tkinter.IntVar()
        first = tkinter.StringVar()

        def get_rows_and_cols(r, c, f):
            Const.ROWS = r.get()
            Const.COLS = c.get()
            Const.PLAYER_TURN = bool(f.get())
            Const.START = True
            Const.HORIZONTAL_PLAYER_MOVES = [ (1,1), (1,2), (1,3), (1,4), (1,5), (3,1), (3,2), (3,3), (3,4), (3,5), (5,1), (5,2), (5,3), (5,4), (5,5), (Const.COLS-2,1), (Const.COLS-2,2), (Const.COLS-2,3), (Const.COLS-2,4), (Const.COLS-2,5) ]
            Const.VERTICAL_PLAYER_MOVES =[ (0,1), (1,1), (2,1), (3,1), (4,1), (0,3), (1,3), (2,3), (3,3), (4,3), (0,5), (1,5), (2,5), (3,5), (4,5),  (0,Const.ROWS-2), (1,Const.ROWS-2), (2,Const.ROWS-2), (3,Const.ROWS-2), (4,Const.ROWS-2) ]
            root.destroy()

        ttk.Label(frm, text="Rows:", width=5).grid(column=0, row=1)
        ttk.Entry(frm, width=8, textvariable=rows).grid(column=1, row=1, pady=1)
        ttk.Label(frm, text="Cols:", width=5).grid(column=0, row=2)
        ttk.Entry(frm, width=8, textvariable=cols).grid(column=1, row=2, pady=1)
        ttk.Label(frm, text="Play first:").grid(column=0, row=3)
        ttk.Radiobutton(frm, text="Player", variable=first, value=1).grid(column=1, row=3)
        ttk.Radiobutton(frm, text="Computer", variable=first, value="").grid(column=2, row=3)
        ttk.Button(frm, text="Play", command=partial(get_rows_and_cols, rows, cols, first)).grid(column=1, row=4)

        root.mainloop()
