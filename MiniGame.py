from tkinter import *
from random import *
from pokedex import pokemon_lista
from tkinter import messagebox
from PIL import Image,ImageTk
import pygame
import time

root = Tk()
root.title('Quem é este Pokémon?')

pokemon = '' 
indice_fixo = 0
coins = 3

def gera_pokemon():
    
    pygame.init()
    pygame.mixer.music.load('whos.mp3')
    pygame.mixer.music.play()
    
    time.sleep(0.5)
    
    indice = randint(0, 150)
    false_indice_1 = randint(0,150)
    false_indice_2 = randint(0,150)
    
    global indice_fixo 
    indice_fixo = indice

    global pokemon


    pokemon = str(pokemon_lista[indice]['Nome'])
     
    imagem_pokemon = pokemon_lista[indice]['Sprite_sombreada']
    
    render = ImageTk.PhotoImage(file = imagem_pokemon)
    img["image"] = render
    img.image = render

    random_indices = [indice, false_indice_1, false_indice_2]
    shuffle(random_indices)
    
    for indice, rs in zip(random_indices, [r1, r2, r3]):
            rs['text'] = f'{pokemon_lista[indice]["Nome"]}'
            rs['value'] = f'{pokemon_lista[indice]["Nome"]}'

    return pokemon,indice_fixo
    

def descobre():
    global coins

    if pokemon_misterioso.get() == pokemon:  
        
        pygame.init()
        pokemon_sound = pygame.mixer.Sound(file = pokemon_lista[indice_fixo]['Som'])
        pokemon_sound.play()


        coins+=1
        
        time.sleep(2)

        messagebox.showinfo('Olá')

        gera_pokemon()
        
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

pokemon_misterioso = StringVar()

r1 =  Radiobutton(text = '?????', value = '', variable = pokemon_misterioso)
r1.pack()
r1.place(x = 5, y = 280)

r2 = Radiobutton(text = '?????', value = '', variable = pokemon_misterioso)
r2.pack()
r2.place(x = 120, y = 280)

r3 = Radiobutton(text = '?????',value = '',variable = pokemon_misterioso)
r3.pack()
r3.place(x = 235, y = 280)

btn = Button(text = 'inserir',command = descobre)
btn.pack()
btn.place(x = 50, y = 320)

root.geometry("350x400+10+10") 
root.mainloop()
