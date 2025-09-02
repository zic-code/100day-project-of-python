from tkinter import*

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)

#label

my_label = Label(text = "I am a Label", font =("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New word")

#button

def button_clicked():
    my_label.config(text = "Button got clicked!!")

button = Button(text="click me!",command=button_clicked)

button.pack()







window.mainloop()