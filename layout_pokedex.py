from tkinter import *
from pokedex import pokemon_lista

root = Tk()


class Application:
    
    def __init__(self,master=None):
        layout_superior = Label(root, text = '------- Pokedex -------')
        layout_superior.configure(bg = 'blue') #cor da label superior
        layout_superior.pack(side = TOP, expand = False, fill = 'x')

        listagem_pokemon = Listbox(root, selectmode = SINGLE) #div usada para alocar a lista dos nomes e id dos pokemons
        listagem_pokemon.configure(relief = 'groove', border = 5, font = 'Times 12 bold') #configuraçõa de borda de fonte da div e os elemntos dentro dela
        listagem_pokemon.pack(side = LEFT, expand = False, fill = 'both') #localidade, expansão onde a div foi colocada

        def pega_POKEMON(listagem_pokemon):
            w = listagem_pokemon.widget
            index = int(w.curselection()[0])

            tipo = pokemon_lista[index]['Tipo']
            altura = pokemon_lista[index]['Altura']
            peso = pokemon_lista[index]['Peso']

            return tipo, altura, peso            


        div_1 = Scrollbar() #metedo de barra de rolagem
        div_1.pack(side = RIGHT,fill = 'y') #posição que foi inserido
        div_1.configure(command = listagem_pokemon.yview) #Ligado a div de listagem de pokemon
        listagem_pokemon.configure(yscrollcommand = div_1.set) #sentido da rolagem
        listagem_pokemon.bind('<<ListboxSelect>>', pega_POKEMON)

        for id_pokemon, pokemon in enumerate(pokemon_lista): #laço para gerar ordenar os nome e id dos pokemon
            texto = f'#{id_pokemon + 1:0>3}  -  {pokemon["Nome"]}' #variavel onde é armazenado o id e o nome dos pokemon pelo laço
            listagem_pokemon.insert(END,texto) #metodo que insere esses dados na div


        div_2 = Canvas(bg = "black") #div onde será inserido as imagens
        div_2.pack() 
        div_2['width'] = 300 #largura 
        div_2['height'] = 150 # altura
        img = PhotoImage(file = "mapa.png") 
        div_2.create_image(0,0, image = img ,anchor = NW)


        tipo, peso, altura = pega_POKEMON()

        div_3 = Label(text = "Tipo : ")
        div_3.configure(font = 'times 18 italic')
        div_3.place(x = 173, y = 173)

        tipo = Label(text = f"{tipo}")
        tipo.configure(font = 'times 12 bold')
        tipo.place(x = 265, y = 178)

        div_4 = Label(text = "Peso : ")
        div_4.configure(font = 'times 18 italic')
        div_4.place(x = 173, y = 200)

        peso = Label(text = "------")
        peso.configure(font = 'times 12 bold')
        peso.place(x = 265, y = 200)

        div_5 = Label(text = "Altura : ")
        div_5.configure(font = 'times 18 italic')
        div_5.place(x = 173, y = 227)

        altura = Label(text = "------")
        altura.configure(font = 'times 12 bold')
        altura.place(x = 265, y = 230)

root.geometry("360x520+10+10")
Application(root)
root.mainloop()