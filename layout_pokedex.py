from tkinter import *
from pokedex import pokemon_lista
from PIL import Image,ImageTk
root = Tk()


class Application:
    
    def __init__(self,master=None):

        def pega_POKEMON(listagem_pokemon):
            pokemon = listagem_pokemon.widget
            index = int(pokemon.curselection()[0])

            tipo_pokemon = f'{pokemon_lista[index]["Tipo"]}'
            tipo["text"] = str(tipo_pokemon)

            altura_pokemon = f'{pokemon_lista[index]["Altura"]} m'
            altura["text"] = str(altura_pokemon)

            peso_pokemon = f'{pokemon_lista[index]["Peso"]} kg'
            peso["text"] = str(peso_pokemon)

        layout_superior = Label(root, text = '------- Pokedex -------')
        layout_superior.configure(bg = 'blue') #cor da label superior
        layout_superior.pack(side = TOP, expand = False, fill = 'x')

        listagem_pokemon = Listbox(root, selectmode = SINGLE) #div usada para alocar a lista dos nomes e id dos pokemons
        listagem_pokemon.configure(relief = 'groove', border = 5, font = 'Times 12 bold') #configuraçõa de borda de fonte da div e os elemntos dentro dela
        listagem_pokemon.pack(side = LEFT, expand = False, fill = 'both') #localidade, expansão onde a div foi colocada

        div_1 = Scrollbar() #metodo de barra de rolagem
        div_1.pack(side = RIGHT,fill = 'y') #posição que foi inserido
        div_1.configure(command = listagem_pokemon.yview) #Ligado a div de listagem de pokemon
        listagem_pokemon.configure(yscrollcommand = div_1.set) #sentido da rolagem
        listagem_pokemon.bind('<<ListboxSelect>>', pega_POKEMON)

        for id_pokemon, pokemon in enumerate(pokemon_lista): #laço para gerar ordenar os nome e id dos pokemon
            texto = f'#{id_pokemon + 1:0>3}  -  {pokemon["Nome"]}' #variavel onde é armazenado o id e o nome dos pokemon pelo laço
            listagem_pokemon.insert(END,texto) #metodo que insere esses dados na div

        load = Image.open("mapa.png")
        render = ImageTk.PhotoImage(load) 
        img = Label(image = render)
        img.image = render
        img.pack(side = TOP)
        img["width"] = 210
        img["height"] = 150

        div_3 = Label(text = 'Tipo:' )
        div_3.configure(font = 'times 18 bold')
        div_3.place(x = 173, y = 173)

        tipo = Label(text = "------")
        tipo.configure(font = 'times 12 bold')
        tipo.place(x = 260, y = 178)

        div_4 = Label(text = "Peso:")
        div_4.configure(font = 'times 18 bold')
        div_4.place(x = 173, y = 200)

        peso = Label(text = "------")
        peso.configure(font = 'times 12 bold')
        peso.place(x = 260, y = 200)

        div_5 = Label(text = "Altura:")
        div_5.configure(font = 'times 18 bold')
        div_5.place(x = 173, y = 227)

        altura = Label(text = "------")
        altura.configure(font = 'times 12 bold')
        altura.place(x = 260, y = 230)

root.geometry("400x520+10+10")
Application(root)
root.mainloop()