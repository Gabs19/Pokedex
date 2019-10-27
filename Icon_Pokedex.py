from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

root = Tk()
root.title("Teste")
root.iconbitmap(r"pokedex1.ico")

class app:
    def __init__(self,master = None):
        self.canvas = Canvas(root)
        self.canvas["width"] = 400
        self.canvas["height"] = 400
        self.canvas.pack()

        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('3D/bulbasaur.gif'))]
        image = canvas.create_image(200,200, image = sequence[0])
        animating = True
        self.animate(0)

    def animate(self,counter):
        self.canvas.itemconfig(image, image = sequence[counter])
        if not animating:
            return
        after(33,lambda: animate((counter + 1) % len(sequence)))

app(root)
root.geometry("500x520+10+10")
root.mainloop()