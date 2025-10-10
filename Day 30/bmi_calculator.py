from tkinter import *
from tkinter import messagebox

import math

from numpy.ma import minimum

#FileNotFound Error
# with open("a_file.txt")as file :
#       file.read()
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key", "value"}
#     # print(a_dictionary["sdfasdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an Error that I made up")
# #KeyError
# a_dictionary  = {"key": "value"}
# key = a_dictionary["non_exist_key"]

#IndexErrror(list index out of range)
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)



minimum_healthy_bmi = 18.5
maximum_healthy_bmi = 22.5

#Calculator
def bmi_calculator(height, weight):
    if len(height)==0 or len(weight)==0  :
        messagebox.showinfo(title="OOps!", message="Please fill out all the blanks!")
    height = float(int(height) / 100)
    weight = int(weight)
    bmi = round(weight / height **2,2)
    label_canvas1.config(text= f"Your bmi is {bmi}")
    healthy_bmi(height, weight)

def healthy_bmi(height, weight):
    min_weight = minimum_healthy_bmi * height **2
    max_weight = maximum_healthy_bmi * height **2
    proper_weight= round((min_weight+max_weight)/2,2)
    label_canvas2 = Label(text = f"{proper_weight}kg is \n your proper weight ")
    canvas.create_window(280, 125, window=label_canvas2)

# UI Setup
window =Tk()
window.title("BMI calculator")
window.config(padx=40, pady=30)

## size setup
canvas = Canvas(width = 300, height =200)
canvas.grid(column=2, row=0)
### logo setup
bmi_icon = PhotoImage(file= "bmi.png")
bmi_icon = bmi_icon.subsample(3)
canvas.create_image(100,100,image = bmi_icon)
canvas.grid(column=1, row = 0)

#label on canvas
label_canvas1= Label(text = "Check your BMI")
canvas.create_window(280, 100, window = label_canvas1)
#label
height_label = Label(text ="Height")
height_label.grid(column=0,row =1)
weight_label = Label(text ="Weight")
weight_label.grid(column=0, row =2)

#Entry
height_entry = Entry(width=36)
height_entry.grid(column=1, row= 1)
height_entry.focus()
weight_entry = Entry(width=36)
weight_entry.grid(column=1, row= 2)

#Button
calculate_button = Button(width=21, text="Calculate", command = lambda:bmi_calculator(height_entry.get(),weight_entry.get()))
calculate_button.grid(column=1, row =3)



window.mainloop()
