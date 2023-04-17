from tkinter import *
from home_page import home_page
from recover_account_page import *
from new_page import *
import sqlite3


class log_in:
    def __init__(self):
        self.email = StringVar()
        self.password = StringVar()
        self.color_box = Label(text=' ', width=30, height=20, bg='#A7D9DB', highlightbackground='black',
                               highlightthickness=2,)
        self.title_label = Label(text='Account details', font=('Aerial', 14), bg='#A7D9DB')
        self.email_label = Label(text='Email:', font=('Aerial', 12), bg='#A7D9DB')
        self.email_entry = Entry(width=25, textvariable=self.email)
        self.password_label = Label(text='Password:', font=('Aerial', 12), bg='#A7D9DB')
        self.password_entry = Entry(width=20, show='*', textvariable=self.password)
        self.incorrect_label = Label(text='Incorrect account details', font=('Aerial', 14), bg='#457B9D')

        def wipe():
            self.color_box.place_forget()
            self.title_label.place_forget()
            self.email_label.place_forget()
            self.email_entry.place_forget()
            self.incorrect_label.place_forget()

        def create_connection(path):
            connection = None
            try:
                connection = sqlite3.connect(path)
                print("Connection to SQLite DB successful")
            except sqlite3.Error as e:
                print(e)

            return connection

        def access():
            conn = create_connection('database.db')
            correct = check_login(conn, self.email.get(), self.password.get())
            if correct:
                wipe()
                new_page('#457B9D',
                         '#A7D9DB')
                home_page(correct)
            else:
                self.incorrect_label.place(x=150, y=50)

        # Creates a user inserting into the table, based off customer parameter
        def check_login(conn, user, password):
            sql = """SELECT customerID from customers where (email=? and Password=?)"""
            cur = conn.cursor()
            cur.execute(sql, [user, password])
            conn.commit()
            try:
                return cur.fetchall()[0][0]
            except IndexError:
                return 0

        self.log_in_button = Button(text='Log in', font=('Aerial', 15), highlightbackground='black',
                                    highlightthickness=2, bg='#F1FAEE', command=lambda: access())

        def wipe():
            self.color_box.place_forget()
            self.title_label.place_forget()
            self.email_label.place_forget()
            self.email_entry.place_forget()
            self.password_label.place_forget()
            self.password_entry.place_forget()
            self.log_in_button.place_forget()
            self.forgot_button.place_forget()

        self.forgot_button = Button(text='Forgot username or password', font=('Aerial', 10), highlightbackground='black'
                                    , highlightthickness=2, bg='#F1FAEE', command=lambda: [wipe(), new_page('#F1FAEE',
                                                                                                            '#457B9D'),
                                                                                           recover_account()])

        self.color_box.place(x=240, y=100)
        self.title_label.place(x=280, y=105)
        self.email_label.place(x=245, y=180)
        self.email_entry.place(x=295, y=183)
        self.password_label.place(x=245, y=230)
        self.password_entry.place(x=327, y=233)
        self.log_in_button.place(x=315, y=315)
        self.forgot_button.place(x=260, y=370)