from tkinter import *

# Function Called after Button Click
def hello():
    print("Hello World")
    print(t1.get())

# Create the main window
window = Tk()
window.geometry("500x500")
window.title("My GUI")

# Create a label widget
label = Label(window, text="Hello, World!", fg="red", font="comicsansms 19 bold")
label.pack()

# Create a button widget
button = Button(window, text="Click Me", command=hello)
button.pack()

t1 = StringVar()
entry = Entry(window, textvariable=t1)
entry.pack()

window.mainloop()