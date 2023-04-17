from tkinter import *
from first_page_color import *
from new_page import *
from first_page import *
import sqlite3


class create_window:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.resizable(False, False)
        self.start_page = first_page()
        self.root.mainloop()


if __name__ == '__main__':
    root = create_window()