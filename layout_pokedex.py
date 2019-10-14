from tkinter import *
from pokedex import pokemon_lista

root = Tk()

class Application:
    def __init__(self,master=None):
        layout_superior = Label(root, text = '------- Pokedex -------')
        layout_superior.configure(bg = 'red')
        layout_superior.pack(side = TOP, expand = False, fill = 'x')

        listagem_pokemon = Listbox() #div usada para alocar a lista dos nomes e id dos pokemons
        listagem_pokemon.configure(relief = 'groove', border = 10, font = 'Times 12 bold') #configuraçõa de borda de fonte da div e os elemntos dentro dela
        listagem_pokemon.pack(side = LEFT, expand = False, fill = 'both') #localidade, expansão onde a div foi colocada

        div_1 = Scrollbar() #metedo de barra de rolagem
        div_1.pack(side = RIGHT,fill = 'y') #posição que foi inserido
        div_1.configure(command = listagem_pokemon.yview) #Ligado a div de listagem de pokemon
        listagem_pokemon.configure(yscrollcommand = div_1.set) #sentido da rolagem

        for id_pokemon, pokemon in enumerate(pokemon_lista): #laço para gerar ordenar os nome e id dos pokemon
            texto = f'#{id_pokemon + 1:0>3}  -  {pokemon["Nome"]}' #variavel onde é armazenado o id e o nome dos pokemon pelo laço
            listagem_pokemon.insert(END,texto) #metodo que insere esses dados na div

        div_2 = Canvas(bg = "black") #div onde será inserido as imagens
        div_2.pack() 
        div_2['width'] = 300 #largura 
        div_2['height'] = 150 # altura
        img = PhotoImage(file = "mapa.png") 
        div_2.create_image(0,0, image = img ,anchor = NW)

root.geometry("360x520+10+10")
Application(root)
root.mainloop()