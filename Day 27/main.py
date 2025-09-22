from tkinter import*

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)

#label

my_label = Label(text = "I am a Label", font =("Arial", 24, "italic"))
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"
my_label.config(text = "New word")

#button

def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)


button = Button(text="click me!",command=button_clicked)
button.grid(column=2,row=1)

new_button = Button(text = "new Button!", command = button_clicked)
button.grid(column=2, row =0)


#Entry
input = Entry()
input.grid(column=2,row=2)
print(input.get())





window.mainloop()