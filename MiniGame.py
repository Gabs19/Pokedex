from tkinter import *
from random import *
import tkinter as tk
from pokedex import pokemon_lista
from PIL import Image,ImageTk
import pygame
import threading

root = Tk()
root.title('Quem é este Pokémon?')

pokemon = '' 

indice = 0

coins = 3


def gera_pokemon():
    global indice
    
    indice = randint(0, 150)
    false_indice_1 = randint(0,150)
    false_indice_2 = randint(0,150)
    
    global pokemon
    
    pokemon = str(pokemon_lista[indice]['Nome'])
     
    imagem_pokemon = pokemon_lista[indice]['Sprite']
    
    render = ImageTk.PhotoImage(file = imagem_pokemon)
    img["image"] = render
    img.image = render
    

    r1['text'] = str(f'{pokemon_lista[indice]["Nome"]}')
    r1['value'] = str(f'{pokemon_lista[indice]["Nome"]}') 
    
    r2['text'] = str(f'{pokemon_lista[false_indice_1]["Nome"]}')
    r2['value'] = str(f'{pokemon_lista[false_indice_1]["Nome"]}') 
    
    r3['text'] = str(f'{pokemon_lista[false_indice_2]["Nome"]}')
    r3['value'] = str(f'{pokemon_lista[false_indice_2]["Nome"]}') 
    
       
    return pokemon,indice
    
def descobre():
    global coins
    
    if i.get() == pokemon:  
        
        pygame.init()
        pokemon_sound = pygame.mixer.Sound(file = pokemon_lista[indice]['Som'])
        pokemon_sound.play()
        
        coins+=1
        
        timer = threading.Timer(2.0,gera_pokemon)
        timer.start()
        
        print(f'funfou {coins}')
        
            
    else:
        if coins == 0:
            coins = 0
        else:
            coins-=1
        
        gera_pokemon() 

        print(f'não funfou, {coins}')   
    
    coin['text'] = str(f'Coins: {coins}')

start = Button(text = 'Start', command = gera_pokemon)
start.pack()
start.place(x = 10, y = 20)
start.configure()

coin = Label(text = f'Coins: {coins}')
coin.pack()
coin.place(x = 260, y = 20)


load = Image.open("noid.png")
render = ImageTk.PhotoImage(load)


img = Label(image = render)
img.place(x = 80, y = 50)
img.configure(relief = 'groove', border = 3,bg = 'white')
img['width'] = 200
img['height'] = 200

i = StringVar()

r1 =  Radiobutton(text = '?????', value = '', variable = i)
r1.pack()
r1.place(x = 5, y = 280)

r2 = Radiobutton(text = '?????', value = '', variable = i)
r2.pack()
r2.place(x = 120, y = 280)

r3 = Radiobutton(text = '?????',value = '',variable = i)
r3.pack()
r3.place(x = 235, y = 280)

btn = Button(text = 'inserir',command = descobre)
btn.pack()
btn.place(x = 50, y = 320)

root.geometry("350x400+10+10") 
root.mainloop()