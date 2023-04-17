from tkinter import *



class recover_account_notice:
    def __init__(self):
        self.color_box = Label(text=' ', width=40, height=20, bg='#A7D9DB', highlightbackground='black',
                               highlightthickness=2)
        self.title_label = Label(text='Notice', font=('Aerial', 16), bg='#A7D9DB')
        self.notice_label = Label(text="""A recovery email has been sent
to your inbox along with your username.
Please close and re-open the program to log in""", font=('Aerial', 10), bg='#A7D9DB')

        self.color_box.place(x=200, y=100)
        self.title_label.place(x=317, y=105)
        self.notice_label.place(x=210, y=230)