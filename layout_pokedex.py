from tkinter import *
from pokedex import pokemon_lista

root = Tk()

class Application:
    def __init__(self,master=None):
        layout_superior = Label(root, text = '------- Pokedex -------')
        layout_superior.pack(side = TOP, expand = False, fill = 'x')

        listagem_pokemon = Listbox()
        listagem_pokemon.configure(relief = 'groove', border = 10, font = 'Times 12 bold')
        listagem_pokemon.pack(side = LEFT, expand = False, fill = 'both')

        div_1 = Scrollbar()
        div_1.pack(side = RIGHT,fill = 'y')
        div_1.configure(command = listagem_pokemon.yview)
        listagem_pokemon.configure(yscrollcommand = div_1.set)

        div_2 = Canvas(bg = "black")
        div_2.pack()
        div_2['width'] = 300
        div_2['height'] = 150
        img = PhotoImage(file = "C://Users//Gabriel//Desktop//IFPE - ADS//projeto//Pokedex//mapa.png")
        div_2.create_image(0,0, image = img ,anchor = NW)

        for id_pokemon, pokemon in enumerate(pokemon_lista):
            texto = f'#{id_pokemon + 1:0>3}  -  {pokemon["Nome"]}'
            listagem_pokemon.insert(END,texto)

root.geometry("360x520+10+10")
Application(root)
root.mainloop()