from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


class GameForm:

    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root,padding=20)
        frm.grid()
        root.title("Domineering")
        rows = tkinter.IntVar()
        cols = tkinter.IntVar()
        first = tkinter.StringVar()
        
        def getRowsANDCols(r:Entry, c:Entry, f:Radiobutton):
            ROWS= r.get()
            COLS= c.get()
            FIRST_PLAYER= f.get()
            print("s")


        ttk.Label(frm, text="Rows:", width=5).grid(column=0, row=1)
        ttk.Entry(frm, width=8, textvariable=rows).grid(column=1, row=1, pady=1)

        ttk.Label(frm, text="Cols:", width=5).grid(column=0, row=2)
        ttk.Entry(frm, width=8, textvariable=cols).grid(column=1, row=2, pady=1)

        ttk.Label(frm, text="Play first:").grid(column=0, row=3)

        ttk.Radiobutton(frm, text="Player", variable = first, value = 0).grid(column=1, row=3)
        ttk.Radiobutton(frm, text="Computer", variable = first, value = 1).grid(column=2, row=3)

        getRowsANDCols = partial(getRowsANDCols, rows, cols, first)
        ttk.Button(frm, text="Play", command = getRowsANDCols).grid(column=1, row=4)

        root.mainloop()

c = GameForm()