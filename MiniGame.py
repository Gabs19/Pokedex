from tkinter import *
from random import *
from pokedex import pokemon_lista
from tkinter import messagebox
from PIL import Image,ImageTk
import pygame
import time

root = Tk()
root.title('Quem é este Pokémon?')

#variaves globais para funcioanmento do central do jogo
pokemon = '' 
indice_fixo = 0
coins = 0

#função que ira gerar o pokemon misterioso e seu indices no dicionario, além de iniciar tdo o jogo
def gera_pokemon():
    
    pygame.init()#inicia o pygame
    pygame.mixer.music.load('whos.mp3')#ler o arquivo de audio na maquina
    pygame.mixer.music.play()#toca o arquivo
    
    time.sleep(0.5)#espera meio segundo para ser executado todo o resto do código
    
    #gerando aleatoriamente os indices para o jogo
    indice = randint(0, 150)#o unico indice certo
    false_indice_1 = randint(0,150)
    false_indice_2 = randint(0,150)
    
    global indice_fixo 
    indice_fixo = indice #mantém o indice original guardado

    global pokemon

    pokemon = str(pokemon_lista[indice]['Nome']) #gera o nome do pokemon que ira ser descoberto
     
    imagem_pokemon = pokemon_lista[indice]['Sprite_sombreada'] #chama a imagem obscurecida do pokemon
    

    render = ImageTk.PhotoImage(file = imagem_pokemon)
    img["image"] = render
    img.image = render
    
    #shuffles funçaõ para embaralhar
    random_indices = [indice, false_indice_1, false_indice_2]
    shuffle(random_indices)
    
    #laço para embaralhar as alternativas para adivinhação 
    for indice, rs in zip(random_indices, [r1, r2, r3]):
            rs['text'] = f'{pokemon_lista[indice]["Nome"]}'
            rs['value'] = f'{pokemon_lista[indice]["Nome"]}'

    return pokemon,indice_fixo

#função que inseri a imagem colorida do pokemon caso ele for descoberto   
def show_pokemon():

    imagem_pokemon = pokemon_lista[indice_fixo]['Sprite']
    
    render = ImageTk.PhotoImage(file = imagem_pokemon)
    img["image"] = render
    img.image = render

def descobre():
    global coins #quantos pontos o jogador marcou

    if pokemon_misterioso.get() == pokemon:  
        
        pygame.init()
        pokemon_sound = pygame.mixer.Sound(file = pokemon_lista[indice_fixo]['Som'])
        pokemon_sound.play()

        coins+=1
        
        time.sleep(2)

        messagebox.showinfo(title = 'Acertou',message = show_pokemon())

        gera_pokemon()
        
        print(f'funfou {coins}')
        
            
    else:
        if coins == 0:
            coins = 0
        else:
            coins-=1
        
        gera_pokemon() 

        messagebox.showinfo(title='Errou')
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

pokemon_misterioso = StringVar() #variavel que passada como valor dentro dos radiobuttons

#conjunto de radiobuttons que saõ usados para desvendar o pokemon misterioso
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