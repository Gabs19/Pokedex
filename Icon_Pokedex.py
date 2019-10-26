from tkinter import *
import tkinter as tk
from time import sleep

root = Tk()
root.title("Teste")
root.iconbitmap(r"pokedex1.ico")

def task():
    # The window will stay open until this function call ends.
    sleep(5) # Replace this with the code you want to run
    root.destroy()

label = Label(root, text="Waiting for task to finish.")
label.pack()


root.after(100, task)
root.geometry("500x520+10+10")
root.mainloop()


print('rodando...')