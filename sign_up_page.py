from tkinter import *
from home_page import home_page
from new_page import new_page
import sqlite3
import pandas as pd
from sqlite3 import Error


class sign_up:
    def __init__(self):
        self.color_box = Label(text=' ', width=30, height=20, bg='#A7D9DB', highlightbackground='black',
                               highlightthickness=2,)
        self.title_label = Label(text='Account details', font=('Aerial', 14), bg='#A7D9DB')
        self.email_label = Label(text='Email:', font=('Aerial', 12), bg='#A7D9DB')
        self.email_entry = Entry(width=25)
        self.username_label = Label(text='Username:', font=('Aerial', 12), bg='#A7D9DB')
        self.username_entry = Entry(width=20)
        self.password_label = Label(text='Password:', font=('Aerial', 12), bg='#A7D9DB')
        self.password_entry = Entry(width=20, show='*')
        self.location_label = Label(text='Location:', font=('Aerial', 12), bg='#A7D9DB')
        self.location_entry = Entry(width=20)

        def wipe():
            self.color_box.place_forget()
            self.title_label.place_forget()
            self.email_label.place_forget()
            self.email_entry.place_forget()
            self.username_label.place_forget()
            self.username_entry.place_forget()
            self.password_label.place_forget()
            self.password_entry.place_forget()
            self.create_account_button.place_forget()
            self.location_label.place_forget()
            self.location_entry.place_forget()

        self.create_account_button = Button(text='Create account', font=('Aerial', 15), highlightbackground='black',
                                            highlightthickness=2, bg='#457B9D', command=lambda: [wipe(),
                                                                                                 new_page('#457B9D',
                                                                                                          '#A7D9DB'),
                                                                                                 main()])

        self.color_box.place(x=240, y=100)
        self.title_label.place(x=280, y=105)
        self.email_label.place(x=245, y=160)
        self.email_entry.place(x=295, y=163)
        self.username_label.place(x=245, y=205)
        self.username_entry.place(x=327, y=208)
        self.password_label.place(x=245, y=250)
        self.password_entry.place(x=327, y=253)
        self.create_account_button.place(x=275, y=340)
        self.location_label.place(x=245, y=290)
        self.location_entry.place(x=315, y=293)

        # Establishes a connection to the sql database, prints error if failure to connect.
        def create_connection(path):
            connection = None
            try:
                connection = sqlite3.connect(path)
                print("Connection to SQLite DB successful")
            except Error as e:
                print(e)

            return connection

        # Creates a table from SQL connection, and from a query
        def create_table(conn, create_table_sql):
            try:
                c = conn.cursor()
                c.execute(create_table_sql)
            except Error as e:
                print(e)

        def check_login(conn, user, password):
            sql = """SELECT customerID from customers where (email=? and Password=?)"""
            cur = conn.cursor()
            cur.execute(sql, [user, password])
            conn.commit()
            try:
                return cur.fetchall()[0][0]
            except IndexError:
                return 0

        # Creates a user inserting into the table, based off customer parameter
        def create_user(conn, customer):
            sql = """INSERT INTO customers(email, username, password, location)
                     VALUES(?,?,?,?)"""
            cur = conn.cursor()
            cur.execute(sql, customer)
            conn.commit()
            return cur.lastrowid

        # Main function, path of database is database.db and creation table query for a customer ID, firstname,
        # lastname and email. SQLite will then attempt to connect and add 2 users to the table.
        def main():

            sql_create_projects_tabel = """CREATE TABLE IF NOT EXISTS customers(customerID integer PRIMARY KEY,
             email text NOT NULL, username text NOT NULL, password text NOT NULL, location text NOT NULL);"""

            conn = create_connection(r'database.db')

            if conn is not None:
                create_table(conn, sql_create_projects_tabel)
                user = (self.email_entry.get(), self.username_entry.get(), self.password_entry.get(),
                        self.location_entry.get().capitalize())
                create_user(conn, user)
                df = pd.read_sql_query("SELECT * FROM customers", conn)
                print(df)
                home_page(check_login(conn, self.email_entry.get(), self.password_entry.get()))
            else:
                print('error')

        if __name__ == "__main__":
            main()