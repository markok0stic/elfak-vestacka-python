from tkinter import *
from tkinter import ttk

class GameForm:

    def __init__(self):
        root = Tk()
        frm = ttk.Frame(root,padding=20)
        frm.grid()

        ttk.Label(frm, text="Rows:", width=5).grid(column=0, row=1)
        ttk.Spinbox(frm, width=5).grid(column=1, row=1, pady=1)

        ttk.Label(frm, text="Cols:", width=5).grid(column=0, row=2)
        ttk.Spinbox(frm, width=5).grid(column=1, row=2, pady=1)

        ttk.Label(frm, text="Select opponent").grid(column=0, row=3)

        ttk.Radiobutton(frm, text="Player").grid(column=1, row=3)
        ttk.Radiobutton(frm, text="Computer").grid(column=2, row=3)

        ttk.Button(frm, text="Play").grid(column=1, row=4)

        root.mainloop()

c = GameForm()