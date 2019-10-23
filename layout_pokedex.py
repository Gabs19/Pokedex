from tkinter import *
import tkinter as tk
from pokedex import pokemon_lista
from PIL import Image,ImageTk

root = Tk()
root.title("POKEDEX")
root.iconbitmap(r"pokedex1.ico")

class Application:
    
    def __init__(self,master=None):

        def pega_POKEMON(listagem_pokemon): #função que executada ao clicar em um elemento da listbox com botão direito do mouse
            pokemon = listagem_pokemon.widget #selecionando o widget da listBox para selecionar um item apenas
            index = int(pokemon.curselection()[0]) #função index utilizada para pegar o index e comparar com a da lista de pokemon


            tipo_pokemon_1 = f'{pokemon_lista[index]["Tipo_1"]}' #Varivel onde está guardado a formatação do index pego pelo bind na listbox
            tipo["text"] = str(tipo_pokemon_1) #Substituição do valor no tipo que é apresentado na tela dinamicamente


            #estrututas de repetições que colocam cores respectivamente ao tipo do pokemon
            if tipo_pokemon_1 == 'Fogo':
                tipo["bg"] = '#ED6D12'
            
            elif tipo_pokemon_1 == 'Água':
                tipo["bg"] = '#4578ED'
               
            elif tipo_pokemon_1 == 'Planta':
                tipo["bg"] = '#69C23D'

            elif tipo_pokemon_1 == 'Voador':
                tipo["bg"] = '#8E6FEB'

            elif tipo_pokemon_1 == 'Normal':
                tipo["bg"] = '#9C9C63'
            
            elif tipo_pokemon_1 == 'Elétrico':
                tipo["bg"] = '#F6C913'
            
            elif tipo_pokemon_1 == 'Terra':
                tipo["bg"] = '#DBB54D'
            
            elif tipo_pokemon_1 == 'Aço':
                tipo["bg"] = '#A0A0C0'
            
            elif tipo_pokemon_1 == 'Inseto':
                tipo["bg"] = '#97A51D'
            
            elif tipo_pokemon_1 == 'Rocha':
                tipo["bg"] = '#A48F32'

            elif tipo_pokemon_1 == 'Gelo':
                tipo["bg"] = '#7ECECE'

            elif tipo_pokemon_1 == 'Lutador':
                tipo["bg"] = '#AE2A24'
            
            elif tipo_pokemon_1 == 'Venenoso':
                tipo["bg"] = '#923A92'

            elif tipo_pokemon_1 == 'Noturno':
                tipo["bg"] =  '#644E40'

            elif tipo_pokemon_1 == 'Fantasma':
                tipo["bg"] = '#655E88'
            
            elif tipo_pokemon_1 == 'Dragão':
                tipo["bg"] = '#5E1DF7'

            elif tipo_pokemon_1 == 'Psíquico':
                tipo["bg"] = '#F73670'

            elif tipo_pokemon_1 == 'Fada':
                tipo["bg"] = '#e87890'

            tipo_pokemon_2 = f'{pokemon_lista[index]["Tipo_2"]}'
            tipo_secundario["text"] = str(tipo_pokemon_2)

            if tipo_pokemon_2 == "":
                tipo_secundario["bg"] = 'white'
            
            #
            elif tipo_pokemon_2 != "":

                if tipo_pokemon_2 == 'Fogo':
                    tipo_secundario["bg"] = '#ED6D12'
                
                elif tipo_pokemon_2 == 'Água':
                    tipo_secundario["bg"] = '#4578ED'
                
                elif tipo_pokemon_2 == 'Planta':
                    tipo_secundario["bg"] = '#69C23D'

                elif tipo_pokemon_2 == 'Voador':
                    tipo_secundario["bg"] = '#8E6FEB'

                elif tipo_pokemon_2 == 'Normal':
                    tipo_secundario["bg"] = '#9C9C63'
                
                elif tipo_pokemon_2 == 'Elétrico':
                    tipo_secundario["bg"] = '#F6C913'
                
                elif tipo_pokemon_2 == 'Terra':
                    tipo_secundario["bg"] = '#DBB54D'
                
                elif tipo_pokemon_2 == 'Aço':
                    tipo_secundario["bg"] = '#A0A0C0'
                
                elif tipo_pokemon_2 == 'Inseto':
                    tipo_secundario["bg"] = '#97A51D'
                
                elif tipo_pokemon_2 == 'Rocha':
                    tipo_secundario["bg"] = '#A48F32'

                elif tipo_pokemon_2 == 'Gelo':
                    tipo_secundario["bg"] = '#7ECECE'

                elif tipo_pokemon_2 == 'Lutador':
                    tipo_secundario["bg"] = '#AE2A24'
                
                elif tipo_pokemon_2 == 'Venenoso':
                    tipo_secundario["bg"] = '#923A92'

                elif tipo_pokemon_2 == 'Noturno':
                    tipo_secundario["bg"] =  '#644E40'

                elif tipo_pokemon_2 == 'Fantasma':
                    tipo_secundario["bg"] = '#655E88'
                
                elif tipo_pokemon_2 == 'Dragão':
                    tipo_secundario["bg"] = '#5E1DF7'

                elif tipo_pokemon_2 == 'Psíquico':
                    tipo_secundario["bg"] = '#F73670'

                elif tipo_pokemon_2 == 'Fada':
                    tipo_secundario["bg"] = '#e87890'

            #Troca dinamicamente as dados dos pokemon a cada item selecionado
            nome["text"] = str(f'{pokemon_lista[index]["Nome"]}')
            altura["text"] = str(f'{pokemon_lista[index]["Altura"]} m')
            peso["text"] = str(f'{pokemon_lista[index]["Peso"]} kg')

            #Troca dinamicamente as imagens dos pokemon a cada item selecionado
            render = ImageTk.PhotoImage(file = pokemon_lista[index]['Sprite'])
            img["image"] = render
            img.image = render

        layout_superior = Label(root, text = '------- Pokedex -------') #primeira label na interface
        layout_superior.configure(bg = 'red') #cor da label superior
        layout_superior.pack(side = TOP, expand = False, fill = 'x')#posição em relação ao espaço na tela, e quando ela se expande no eixo X

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

        load = Image.open("noid.png")
        render = ImageTk.PhotoImage(load) 
        img = Label(image = render)
        img.image = render
        img.place(x = 180, y = 30)
        img["width"] = 80
        img["height"] = 80

        #Dados iniciais : imagem, nome, tipo.
        img = Label(image = "")
        img.place(x = 180 , y = 30)

        nome = Label(text = "???????")
        nome.configure(font = 'times 14 bold')
        nome.place(x = 290, y = 35)
    
        tipo = Label(text = "??????")
        tipo.configure(font = 'times 12 bold')
        tipo.place(x = 290, y = 70)

        tipo_secundario = Label(text = '??????')
        tipo_secundario.configure(font = 'times 12 bold')
        tipo_secundario.place(x = 370, y = 70)

        div_6 = Label(text = "----- Dados -----") #Label que separa dados iniciais dos dados detalhados
        div_6.configure(bg = 'red')#cor do background
        div_6.place(x = 174, y = 140)

        weight = Label(text = 'Peso:')
        weight.configure(font = 'times 12 bold')
        weight.place(x = 175, y = 180)

        peso = Label(text = "???? kg")
        peso.configure(font = 'times 12')
        peso.place(x = 230, y = 180)
        
        heigth = Label(text = 'Altura:')
        heigth.configure(font = 'times 12 bold')
        heigth.place(x = 310, y = 180 )

        altura = Label(text = "??? m")
        altura.configure(font = 'times 12')
        altura.place(x = 370, y = 180)
        

        


root.geometry("500x520+10+10") #funçaõ para definir o tamanho que a tela será aberta
Application(root)
root.mainloop() # mantém a interface ligada rodando o codigo, que só fechado quando precionado o botão fechar