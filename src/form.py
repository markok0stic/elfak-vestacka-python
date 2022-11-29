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
   
        def getRowsANDCols(r:Entry, c:Entry, f:Radiobutton):
            global ROWS
            global COLS
            ROWS = r.get()
            COLS = c.get()
            FIRST_PLAYER = f.get()
            root.destroy()

        def getRowsANDCols(r, c, f):
            root.destroy()
            Const.ROWS = r.get()
            Const.COLS = c.get()
            Const.FIRST = f.get()

        ttk.Label(frm, text="Rows:", width=5).grid(column=0, row=1)
        ttk.Entry(frm, width=8, textvariable=rows).grid(column=1, row=1, pady=1)
        ttk.Label(frm, text="Cols:", width=5).grid(column=0, row=2)
        ttk.Entry(frm, width=8, textvariable=cols).grid(column=1, row=2, pady=1)
        ttk.Label(frm, text="Play first:").grid(column=0, row=3)
        ttk.Radiobutton(frm, text="Player", variable=first, value=0).grid(column=1, row=3)
        ttk.Radiobutton(frm, text="Computer", variable=first, value=1).grid(column=2, row=3)
        ttk.Button(frm, text="Play", command=partial(getRowsANDCols, rows, cols, first)).grid(column=1, row=4)

        root.mainloop()
<<<<<<< HEAD
=======

#c = GameForm()
>>>>>>> 285e040de2c1d552e31a5bd9c03aa645302638fc
