from tkinter import *
import tkinter as tk
from pokedex import pokemon_lista
from PIL import Image,ImageTk
# from Icon_Pokedex import *

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

            #estrututas de decisão que colocam cores respectivamente ao tipo do pokemon
            if tipo_pokemon_1 == 'Fogo':
                box_tipo_one["bg"] = '#ED6D12'
                tipo["bg"] = '#ED6D12'
                img["bg"] = '#ED6D12'
            
            elif tipo_pokemon_1 == 'Água':
                box_tipo_one["bg"] = '#4578ED'
                tipo["bg"] = '#4578ED'
                img["bg"] = '#4578ED'
               
            elif tipo_pokemon_1 == 'Planta':
                box_tipo_one["bg"] = '#69C23D'
                tipo["bg"] = '#69C23D'
                img["bg"] = '#69C23D'

            elif tipo_pokemon_1 == 'Voador':
                box_tipo_one["bg"] = '#8E6FEB'
                tipo["bg"] = '#8E6FEB'
                img["bg"] = '#8E6FEB'

            elif tipo_pokemon_1 == 'Normal':
                box_tipo_one["bg"] = '#9C9C63'
                tipo["bg"] = '#9C9C63'
                img["bg"] = '#9C9C63'
            
            elif tipo_pokemon_1 == 'Elétrico':
                box_tipo_one["bg"] = '#F6C913'
                tipo["bg"] = '#F6C913'
                img["bg"] = '#F6C913'
            
            elif tipo_pokemon_1 == 'Terra':
                box_tipo_one["bg"] = '#DBB54D'
                tipo["bg"] = '#DBB54D'
                img["bg"] = '#DBB54D'
            
            elif tipo_pokemon_1 == 'Aço':
                box_tipo_one["bg"] = '#A0A0C0'
                tipo["bg"] = '#A0A0C0'
                img["bg"] = '#A0A0C0'
            
            elif tipo_pokemon_1 == 'Inseto':
                box_tipo_one["bg"] = '#97A51D'
                tipo["bg"] = '#97A51D'
                img["bg"] = '#97A51D'
            
            elif tipo_pokemon_1 == 'Rocha':
                box_tipo_one["bg"] = '#A48F32'
                tipo["bg"] = '#A48F32'
                img["bg"] = '#A48F32'

            elif tipo_pokemon_1 == 'Gelo':
                box_tipo_one["bg"] = '#7ECECE'
                tipo["bg"] = '#7ECECE'
                img["bg"] = '#7ECECE'

            elif tipo_pokemon_1 == 'Lutador':
                box_tipo_one["bg"] = '#AE2A24'
                tipo["bg"] = '#AE2A24'
                img["bg"] = '#AE2A24'

            elif tipo_pokemon_1 == 'Venenoso':
                box_tipo_one["bg"] = '#923A92'
                tipo["bg"] = '#923A92'
                img["bg"] = '#923A92'

            elif tipo_pokemon_1 == 'Noturno':
                box_tipo_one["bg"] =  '#644E40'
                tipo["bg"] =  '#644E40'
                img["bg"] =  '#644E40'

            elif tipo_pokemon_1 == 'Fantasma':
                box_tipo_one["bg"] = '#655E88'
                tipo["bg"] = '#655E88'
                img["bg"] = '#655E88'
            
            elif tipo_pokemon_1 == 'Dragão':
                box_tipo_one["bg"] = '#5E1DF7'
                tipo["bg"] = '#5E1DF7'
                img["bg"] = '#5E1DF7'

            elif tipo_pokemon_1 == 'Psíquico':
                box_tipo_one["bg"] = '#F73670'
                tipo["bg"] = '#F73670'
                img["bg"] = '#F73670'

            elif tipo_pokemon_1 == 'Fada':
                box_tipo_one["bg"] = '#e87890'
                tipo["bg"] = '#e87890'
                img["bg"] = '#e87890'

            tipo_pokemon_2 = f'{pokemon_lista[index]["Tipo_2"]}'
            tipo_secundario["text"] = str(tipo_pokemon_2)

            if tipo_pokemon_2 == "":
                box_tipo_two["bg"] = '#FFFAFA'
                tipo_secundario["bg"] = '#FFFAFA'

            elif tipo_pokemon_2 != "":

                if tipo_pokemon_2 == 'Fogo':
                    box_tipo_two["bg"] = '#ED6D12'
                    tipo_secundario["bg"] = '#ED6D12'
                
                elif tipo_pokemon_2 == 'Água':
                    box_tipo_two["bg"] = '#4578ED'
                    tipo_secundario["bg"] = '#4578ED'
                
                elif tipo_pokemon_2 == 'Planta':
                    box_tipo_two["bg"] = '#69C23D'
                    tipo_secundario["bg"] = '#69C23D'

                elif tipo_pokemon_2 == 'Voador':
                    box_tipo_two["bg"] = '#8E6FEB'
                    tipo_secundario["bg"] = '#8E6FEB'

                elif tipo_pokemon_2 == 'Normal':
                    box_tipo_two["bg"] = '#9C9C63'
                    tipo_secundario["bg"] = '#9C9C63'
                
                elif tipo_pokemon_2 == 'Elétrico':
                    box_tipo_two["bg"] = '#F6C913'
                    tipo_secundario["bg"] = '#F6C913'
                
                elif tipo_pokemon_2 == 'Terra':
                    box_tipo_two["bg"] = '#DBB54D'
                    tipo_secundario["bg"] = '#DBB54D'
                
                elif tipo_pokemon_2 == 'Aço':
                    box_tipo_two["bg"] = '#A0A0C0'
                    tipo_secundario["bg"] = '#A0A0C0'
                
                elif tipo_pokemon_2 == 'Inseto':
                    box_tipo_two["bg"] = '#97A51D'
                    tipo_secundario["bg"] = '#97A51D'
                
                elif tipo_pokemon_2 == 'Rocha':
                    box_tipo_two["bg"] = '#A48F32'
                    tipo_secundario["bg"] = '#A48F32'

                elif tipo_pokemon_2 == 'Gelo':
                    box_tipo_two["bg"] = '#7ECECE'
                    tipo_secundario["bg"] = '#7ECECE'

                elif tipo_pokemon_2 == 'Lutador':
                    box_tipo_two["bg"] = '#AE2A24'
                    tipo_secundario["bg"] = '#AE2A24'
                
                elif tipo_pokemon_2 == 'Venenoso':
                    box_tipo_two["bg"] = '#923A92'
                    tipo_secundario["bg"] = '#923A92'

                elif tipo_pokemon_2 == 'Noturno':
                    box_tipo_two["bg"] =  '#644E40'
                    tipo_secundario["bg"] =  '#644E40'

                elif tipo_pokemon_2 == 'Fantasma':
                    box_tipo_two["bg"] = '#655E88'
                    tipo_secundario["bg"] = '#655E88'
                
                elif tipo_pokemon_2 == 'Dragão':
                    box_tipo_two["bg"] = '#5E1DF7'
                    tipo_secundario["bg"] = '#5E1DF7'

                elif tipo_pokemon_2 == 'Psíquico':
                    box_tipo_two["bg"] = '#F73670'
                    tipo_secundario["bg"] = '#F73670'

                elif tipo_pokemon_2 == 'Fada':
                    box_tipo_two["bg"] = '#e87890'
                    tipo_secundario["bg"] = '#e87890'

            #Troca dinamicamente as dados dos pokemon a cada item selecionado
            nome["text"] = str(f'{pokemon_lista[index]["Nome"]}')
            altura["text"] = str(f'{pokemon_lista[index]["Altura"]} m')
            peso["text"] = str(f'{pokemon_lista[index]["Peso"]} kg')
            descricao["text"] = str(f'{pokemon_lista[index]["Descricao"]}')
            info["text"] = str(f'{pokemon_lista[index]["Info"]}')

            #Troca dinamicamente as imagens dos pokemon a cada item selecionado
            render = ImageTk.PhotoImage(file = pokemon_lista[index]['Sprite'])
            img["image"] = render
            img.image = render

        layout_superior = Label(root, text = '------- Pokedex -------') #primeira label na interface
        layout_superior.configure(bg = 'red') #cor da label superior
        layout_superior.pack(side = TOP, expand = False, fill = 'x')#posição em relação ao espaço na tela, e quando ela se expande no eixo X

        listagem_pokemon = Listbox(root, selectmode = BROWSE) #div usada para alocar a lista dos nomes e id dos pokemons
        listagem_pokemon.configure(relief = 'groove', border = 3, font = 'Times 12 bold',bg = '#FA8072') #configuraçõa de borda de fonte da div e os elemntos dentro dela
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

        #Dados iniciais : imagem, nome, tipo.
        img = Label(image = render)
        img.place(x = 180 , y = 30)
        img.configure(relief = 'groove', border = 3,bg = 'white')
        img["width"] = 90
        img["height"] = 90

        nome = Label(text = "???????")
        nome.configure(font = 'times 14 bold')
        nome.place(x = 290, y = 35)

        box_tipo_one = Canvas()
        box_tipo_one.pack()
        box_tipo_one.configure()
        box_tipo_one["width"] = 80
        box_tipo_one["height"] = 30
        box_tipo_one.place(x = 290, y = 65)
        
        tipo = Label(text = "??????")
        tipo.pack()
        tipo.configure(font = 'times 12 bold')

        box_tipo_one.create_window(41,15,window = tipo)

        box_tipo_two = Canvas()
        box_tipo_two.pack()
        box_tipo_two.configure()
        box_tipo_two["width"] = 80
        box_tipo_two["height"] = 30
        box_tipo_two.place(x = 370, y = 65)

        tipo_secundario = Label(text = '??????')
        tipo_secundario.pack()
        tipo_secundario.configure(font = 'times 12 bold')

        box_tipo_two.create_window(41,15,window = tipo_secundario)


        descricao = Label(text = '??????')
        descricao.configure(font = 'times 12')
        descricao.place(x = 290, y = 100)

        div_6 = Label(text = "----- Dados -----") #Label que separa dados iniciais dos dados detalhados
        div_6.configure(bg = 'red')#cor do background
        div_6.place(x = 174, y = 140)

        #Dados detalhados
        weight = Label(text = 'Peso:')
        weight.configure(font = 'times 12 bold')
        weight.place(x = 175, y = 170)

        peso = Label(text = "???? kg")
        peso.configure(font = 'times 12')
        peso.place(x = 230, y = 170)
        
        heigth = Label(text = 'Altura:')
        heigth.configure(font = 'times 12 bold')
        heigth.place(x = 310, y = 170 )

        altura = Label(text = "??? m")
        altura.configure(font = 'times 12')
        altura.place(x = 370, y = 170)

        habitat = Label(text = "Habitat:")
        habitat.configure(font = 'times 12 bold')
        habitat.place(x = 175, y = 200)

        habilidades = Label(text = "Habilidades:")
        habilidades.configure(font = 'times 12 bold')
        habilidades.place(x = 175, y = 230)

        text_box = Canvas()
        text_box.pack()
        text_box.configure(relief = 'groove', border = 3)
        text_box["width"] = 300
        text_box["height"] = 100
        text_box.place(x = 175, y = 400)
        
        info = Label(text = "", wraplength = 280)
        info.pack()
        info.configure(font = 'times 12')

        text_box.create_window(150,50, window = info )

root.geometry("500x520+10+10") #funçaõ para definir o tamanho que a tela será aberta
Application(root)
root.mainloop() # mantém a interface ligada rodando o codigo, que só fechado quando precionado o botão fechar