from tkinter import *


class first_page_color:
    def __init__(self):
        self.left = Label(text='', width=250, height=500, bg='#457B9D', highlightbackground='black',
                          highlightthickness=2)
        self.right = Label(text='', width=250, height=500, bg='#A7D9DB', highlightbackground='black',
                           highlightthickness=2)
        self.left.place(x=0, y=0)
        self.right.place(x=350, y=0)