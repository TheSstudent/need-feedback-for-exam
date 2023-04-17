from tkinter import *
from first_page_color import *
from new_page import *
from sign_up_page import *
from log_in_page import *


class first_page:
    def __init__(self):
        self.start_color = first_page_color()
        self.signup_header = Label(text='Sign up', font=('consolas', 16, 'bold'), bg='#457B9D')
        self.login_header = Label(text='Sign in', font=('consolas', 16, 'bold'), bg='#A7D9DB')
        self.signup_label = Label(text="""Create an account with us
today so we can help you
enjoy the weather better.""", font=('Consolas', 12), borderwidth=2, highlightbackground='black', highlightthickness=2,
                                  bg='#F1FAEE')
        self.login_label = Label(text="""already have an account?
dont worry sign in here.""", font=('Consolas', 12), borderwidth=2, highlightbackground='black', highlightthickness=2,
                                 bg='#F1FAEE')

        def wipe():
            self.login_label.place_forget()
            self.login_header.place_forget()
            self.login_button.place_forget()
            self.signup_label.place_forget()
            self.signup_header.place_forget()
            self.signup_button.place_forget()

        # creating the login/sign up buttons
        self.login_button = Button(text='Log in', font=('Consolas', 16), borderwidth=2, highlightbackground='black',
                                   highlightthickness=2, bg='#E63946', command=lambda: [wipe(), new_page('#457B9D',
                                                                                                         '#E63946'),
                                                                                        log_in()])
        self.signup_button = Button(text='Start today', font=('Consolas', 16), borderwidth=2,
                                    highlightbackground='black',
                                    highlightthickness=2, bg='#E63946', command=lambda: [wipe(), new_page('#E63946',
                                                                                                          '#457B9D'),
                                                                                         sign_up()])

        # placing objects
        self.login_label.place(x=400, y=105)
        self.signup_label.place(x=55, y=100)
        self.login_button.place(x=470, y=275)
        self.signup_button.place(x=105, y=275)
        self.signup_header.place(x=125, y=20)
        self.login_header.place(x=470, y=15)