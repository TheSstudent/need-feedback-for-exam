from tkinter import *


class new_page:
    def __init__(self, top, bottom):
        self.top = Label(text='', width=500, height=250, bg=top, highlightbackground='black',
                         highlightthickness=2,)
        self.top.place(x=0, y=0)
        self.bottom = Label(text='', width=500, height=250, bg=bottom, highlightbackground='black',
                            highlightthickness=2,)
        self.bottom.place(x=0, y=250)