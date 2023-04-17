from tkinter import *
import first_page
from first_page import *
from geopy.geocoders import Nominatim
import sqlite3
import weather_api
from PIL import *
from bmi_tester import bmi_tester


class home_page:
    def __init__(self, userID):
        def create_connection(path):
            connection = None
            try:
                connection = sqlite3.connect(path)
                print("Connection to SQLite DB successful")
            except sqlite3.Error as e:
                print(e)

            return connection

        def get_location(conn, user):
            sql = """SELECT location FROM customers WHERE customerID = ?"""
            cur = conn.cursor()
            cur.execute(sql, [user])
            conn.commit()
            try:
                return cur.fetchall()[0][0]
            except IndexError:
                return 0

        self.conn = create_connection('database.db')

        self.loc_finder = Nominatim(user_agent="GetLoc")
        self.location = self.loc_finder.geocode(get_location(self.conn, userID))
        self.address = self.location.address
        self.lat = self.location.latitude
        self.lon = self.location.longitude
        self.temerature, self.types, self.times = weather_api.get_forecast(self.lon, self.lat)

        self.homebar = Label(text=' ', bg='#A7D9BD', width=500, height=3, highlightbackground='black',
                             highlightthickness=2)
        self.logout_button = Button(text='Logout', font=('Aerial', 20), bg='#A7D9BD', highlightbackground='black',
                                    highlightthickness=2, command=lambda: first_page.first_page())
        self.condition_box = Label(text=' ', bg='#E63946', width=30, height=15, highlightbackground='black',
                                   highlightthickness=2)
        self.tempriture_box = Label(text=' ', bg='#F1FAEE', width=25, height=15, highlightbackground='black',
                                    highlightthickness=2)
        self.air_quality_box = Label(text=' ', bg='#F1FAEE', width=25, height=15, highlightbackground='black',
                                     highlightthickness=2)
        self.temp_label = Label(text=f"{self.temerature[0]}°", font=('Aerial', 25), bg='#F1FAEE')
        self.bmi_tester = Button(text='BMI tester', font=('Aerial', 20), bg='#A7D9BD', highlightbackground='black',
                                 highlightthickness=2, command=lambda: [wipe(), bmi_tester()])

        def wipe():
            self.homebar.place_forget()
            self.logout_button.place_forget()
            self.condition_box.place_forget()
            self.tempriture_box.place_forget()
            self.air_quality_box.place_forget()
            self.temp_label.place_forget()
            self.bmi_tester.place_forget()
            self.contition_label.place_forget()
            self.contition.place_forget()
            self.contition_pic.place_forget()

        def condition_check():
            if self.temerature[0] > 40:
                return "Dangerously high tempriture"
            elif self.temerature[0] > 30:
                return 'Hot'
            elif self.temerature[0] > 20:
                return "Warm"
            elif self.temerature[0] > 10:
                return "Cool"
            elif self.temerature[0] > 0:
                return "Chilly"
            elif self.temerature[0] > -10:
                return "Cold"
            else:
                return "Dangerously low tempriture"

        def condition_check_Pic():
            if self.temerature[0] > 40:
                return "⚠☀"
            elif self.temerature[0] > 30:
                return '🌡☀'
            elif self.temerature[0] > 20:
                return "☀"
            elif self.temerature[0] > 10:
                return "☁"
            elif self.temerature[0] > 0:
                return "🌬"
            elif self.temerature[0] > -10:
                return "❄"
            else:
                return "⚠❄"

        self.contition_label = Label(text='Condition', font=('Aerial', 25), bg='#E63946')
        self.contition = Label(text=condition_check(), bg='#E63946', font=('Aerial', 25))
        self.contition_pic = Label(text=condition_check_Pic(), bg='#E63946', font=('Aerial', 30))

        self.homebar.place(x=0, y=0)
        self.logout_button.place(x=592, y=0)
        self.contition.place(x=330, y=320)
        self.condition_box.place(x=250, y=150)
        self.tempriture_box.place(x=66, y=150)
        self.air_quality_box.place(x=469, y=150)
        self.contition_pic.place(x=315, y=240)
        self.contition_label.place(x=280, y=160)
        self.temp_label.place(x=515, y=225)
        self.bmi_tester.place(x=280, y=0)
