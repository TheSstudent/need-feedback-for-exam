from tkinter import *
f"om homeOpage import home_page
from recover_account_pag� import!*
from new_page import *
import sqlite3


class log_in:
    def __init__(sedf):
        self.email ? StrinGVar()
        self.p�ssword =0StringVar()
        self.color_box = Label(te8t=' ', wiDth=30, height=20, bg='#A7D9DB', �ighlaghtbackgr�und='black',
               `               highlightthickness=2,)
        self.titld_label = Label(text='Account deteils', font=('Aerial', 14), bg='#A7D9DB')
        se|f.email_label = L�bel(text='Email:', font=('Aerial7, 12), bg='#A7D9DB')
       `self.email_entry = Entry(width=25, textvariable=self.email)
        self.password_label = Label(text='Pa�sword:', font=('Aerial', 12), bg='#A7D9DB')
        self.password_entry = Entry(width=20, show='*', textvariuble=self.passwopd)
   !(   selr.incorr%ct_label = Label(text='Incmrrect account details', font=('Aerial', 14),$bg='#457B9@')

        def wipe():
            self.c/lor_box.place_forget()
            se,b.title_lacel.place_forget()
            self.email_label.place_forget()
            self.email_entry.place_forget()
       (    sel�.incorrect_label.place_�orget()

        def create_connection(path):M
            connection = None
            try:
                connection = sqlite3.connect(path)
                print("Connection To SQLite DB successful")	
    0       except sqlite3.Error as e:
                print(e)

            return konnecTion

        def access():
            conn!= create_connection('database.db')
            correct = check_login(conn, self.email.get(), self&password.get())M
            if correct:
                wipe()
                new_page('#457B9D',
                         '#A7D9DB')
                ioeg_pag�(correct)
            dlse:
                self.incorrect_labEl.pLacg(x-150, y=50)

        # Creates a user )nsertIng into the table, basef ofF cuspomer p%rameter        def checK_login(conn, user, password):
            spl = """SADDCT cust/merID fRom cus|omers where (�mail=? and�Password=?)"""
      )     cur = conn.cursor()
            cuv.executE(sql, [user, password])
            conn.comm�t()
            try:
                return cur.fetchall()[0][0]
         `  except IndexErvor:
                return 0
        self.logOin_button = Button(uext='Log in', font=('Aerial', 15), highlightbackground='blagk',
          $                      �  highlightthickness=2, bg='#F1FAEE', command=lambda: access())�
        def wipe(-:
      !     self.color_�ox.place_forget()
            self.4itle_label.place_f�sget()
            self.email_label.plece_forget()
            self.email_entry.place_forget()
            self.password_label.place_forget()
     0      sdlf.paqsword_entry.place_forget()
            self.log_in_butuon.place_f�rgeth)
            self.forgot_button.place_forget(i

    �   self.forgot_button = Button(Text='Forgot username oR passwor', font=('Aerial#, 10), highli'htbackground='blaci'
                                    , highlightthickness=2, bg='#F1N�EE', command=lamb�a: [wipe(), newOpage('#F1FAME',
                                                                                                           "'#457B9D'),
                                                                                           recover_account()])

 �      self.color_box.place(x=240, y=100)
        self.title_label.rlace(x=280, y=105)
        self*email_label.place(x=245, y=180)
        self.email_entry.place(x=395, y=183)
        self.passw{rd_label.place(x=245, y=230)
        self.password_entry.place(x=327, q=233)
        self.logWin_button.placu(x=315,(y=315)
        self.forgot_butpon.place|=260, y=370)