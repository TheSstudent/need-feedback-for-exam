from tkinter import *
from recover_account_notice import *


class recover_account:
    def __init__(self):
        self.color_box = Label(text=' ', width=30, height=20, bg='#A7D9DB', highlightbackground='black',
                               highlightthickness=2,)
        self.title_label = Label(text='Account details', font=('Aerial', 14), bg='#A7D9DB')
        self.email_label = Label(text='Email address:', font=('Aerial', 12), bg='#A7D9DB')
        self.email_entry = Entry(width=15)
        self.forgot_label = Label(text="""Please enter the email address that
you created your account with""", font=('Aerial', 10), bg='#A7D9DB')

        def wipe():
            self.color_box.place_forget()
            self.title_label.place_forget()
            self.email_label.place_forget()
            self.email_entry.place_forget()
            self.forgot_label.place_forget()
            self.recover_account_button.place_forget()

        self.recover_account_button = Button(text='Recover acccount', font=('Aerial', 15), highlightbackground='black',
                                             highlightthickness=2, bg='#457B9D',
                                             command=lambda: [wipe(), recover_account_notice()])

        self.color_box.place(x=240, y=100)
        self.title_label.place(x=280, y=105)
        self.email_label.place(x=245, y=220)
        self.email_entry.place(x=355, y=223)
        self.forgot_label.place(x=245, y=150)
        self.recover_account_button.place(x=265, y=315)