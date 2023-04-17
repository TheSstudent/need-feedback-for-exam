from tkinter import *


class bmi_tester:
    def __init__(self):
        self.color_box = Label(text=' ', width=30, height=20, bg='#E63946', highlightbackground='black',
                               highlightthickness=2)
        self.title_label = Label(text='BMI tester', bg='#E63946', font=('Aerial', 14))
        self.weight_label = Label(text='Weight(kg):', bg='#E63946', font=('Aerial', 12))
        self.weight_entry = Entry(width=20)
        self.height_label = Label(text='Height(m):', bg='#E63946', font=('Aerial', 12))
        self.height_entry = Entry(width=20)
        self.bmi_button = Button(text='Test BMI', font=('Aerial', 15), highlightbackground='black',
                                 highlightthickness=2, bg='#E63946', command=lambda: result())

        def bmi_check():
            calculate_result = int(self.weight_entry.get()) / float(self.height_entry.get()) **2
            result = round(calculate_result, 2)
            if result > 40:
                return "your BMI is Obese class III"
            elif result > 30:
                return 'your BMI is Obese'
            elif result > 25:
                return "your BMI is Overweight"
            elif result > 18.5:
                return "your BMI is Normal"
            else:
                return "your BMI is Underweight"

        def result():
            self.result = Label(text=bmi_check(), bg='#E63946', font=('Aerial', 12))
            self.result.place(x=280, y=300)

        self.color_box.place(x=240, y=100)
        self.title_label.place(x=290, y=105)
        self.weight_label.place(x=245, y=160)
        self.weight_entry.place(x=330, y=163)
        self.height_label.place(x=245, y=240)
        self.height_entry.place(x=325, y=243)
        self.bmi_button.place(x=300, y=340)
