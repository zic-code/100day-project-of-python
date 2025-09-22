from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

#"websIte| 123456 "
def save():
    website= website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
        "username":username,
        "password":password,
        }
    }

    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="Oops!", message= "Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message = "No Data File Found")
    else:
        if website in data:
            username= data[website]["username"]
            password= data[website]["password"]
            messagebox.showinfo(title =website, message = f"Username: {username}, \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message= f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady =25)

canvas = Canvas(width=200, height = 200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=locker_img)
canvas.grid(column=1, row=0)

#label
website_label = Label(text= "Website")
website_label.grid(column=0,row = 1)
username_label= Label(text="Email/Username")
username_label.grid(column=0, row=2)
password_label = Label(text ="Password")
password_label.grid(column=0,row=3)

#entry

username_entry = Entry(width = 39)
username_entry.grid(column=1, row=2,columnspan=2)
username_entry.insert(0,"leejisoo@outlook.com")
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2)
password_entry=Entry(password_frame, width=21)
password_entry.pack(side="left",ipady=3)
generate_button = Button(password_frame, text = "Generate Password",width=14, command = generate_password)
generate_button.pack(side="left")

# password_entry = Entry(width=21)
# password_entry.grid(column=1,row=3)
# generate_button = Button(text="Generate Password")
# generate_button.grid(column=2,row=3)

add_button = Button(text = "Add",width = 33,command=save)
add_button.grid(column=1, row=4,columnspan=2)
search_frame = Frame(window)
search_frame.grid(column= 1,row = 1 , columnspan = 2)
website_entry = Entry(search_frame,width = 22)
website_entry.pack(side="left",ipady=3)
website_entry.focus()
search_button = Button(search_frame,text = "search", width = 13,command=find_password)
search_button.pack(side="right",ipady=3)




window.mainloop()