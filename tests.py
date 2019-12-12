from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('teste')

var = StringVar()
label = Message( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()