from tkinter import *
from pokedex import pokemon_lista
from PIL import Image,ImageTk
import os
import pygame

root = Tk()
root.title("POKEDEX")
# root.iconbitmap(r"pokedex1.ico")

class Application:
    
    def __init__(self,master=None):
    
        #Troca dinamicamente as dados dos pokemon a cada item selecionado
        def pega_POKEMON(listagem_pokemon): #função que executada ao clicar em um elemento da listbox com botão direito do mouse
            pokemon = listagem_pokemon.widget #selecionando o widget da listBox para selecionar um item apenas
            index = int(pokemon.curselection()[0]) #função index utilizada para pegar o index e comparar com a da lista de pokemon

            nome["text"] = str(f'{pokemon_lista[index]["Nome"]}')
            altura["text"] = str(f'{pokemon_lista[index]["Altura"]} m')
            peso["text"] = str(f'{pokemon_lista[index]["Peso"]} kg')
            descricao["text"] = str(f'{pokemon_lista[index]["Descricao"]}')
            info["text"] = str(f'{pokemon_lista[index]["Info"]}')
            ataque["text"] = str(f'{pokemon_lista[index]["Ataque"]}')
            defesa["text"] = str(f'{pokemon_lista[index]["Defesa"]}')
            velocidade["text"] = str(f'{pokemon_lista[index]["Velocidade"]}')
            sp_ataque["text"] = str(f'{pokemon_lista[index]["Sp.Ataque"]}')
            sp_defesa["text"] = str(f'{pokemon_lista[index]["Sp.Defesa"]}')
            hab["text"] = str(f'{pokemon_lista[index]["Habitat"]}')
            habilities["text"] = str(f'{pokemon_lista[index]["Habilidades"]}')


            #Troca dinamicamente as imagens dos pokemon a cada item selecionado
            render = ImageTk.PhotoImage(file = pokemon_lista[index]['Sprite'])
            img["image"] = render
            img.image = render

            #Toca o som de cada pokemon de acordo com o click
            pygame.init()
            Pokemon_sound = pygame.mixer.Sound(file = pokemon_lista[index]['Som'])
            Pokemon_sound.play()


            #Toca o som de cada pokemon de acordo com o click no botão cry
            def cry_pokemon():
                Pokemon_sound.play()

            cry = Button(text = '< ))',command = cry_pokemon)
            cry.pack()
            cry.place(x = 400, y = 35)
            cry.configure()


            tipo_pokemon_1 = str(f'{pokemon_lista[index]["Tipo_1"]}') #Varivel onde está guardado a formatação do index pego pelo bind na listbox
            tipo["text"] = str(tipo_pokemon_1) #Substituição do valor no tipo que é apresentado na tela dinamicamente

            #dict com tipos e suas cores respectivas
            type_pokemon  = {'Fogo' : '#ED6D12', 'Água' : '#4578ED', 'Planta' : '#69C23D', 'Voador' : '#8E6FEB', 'Normal' : '#9C9C63', 'Elétrico' : '#F6C913', 'Terra' : '#DBB54D', 'Aço' : '#A0A0C0', 'Inseto' : '#97A51D', 'Rocha' : '#A48F32', 'Gelo' : '#7ECECE', 'Lutador' : '#AE2A24', 'Venenoso' : '#923A92', 'Noturno' : '#644E40', 'Fantasma' : '#655E88', 'Dragão' : '#5E1DF7', 'Psíquico' : '#F73670', 'Fada' : '#e87890'}
            
            
            #estrututas de decisão que colocam cores respectivamente ao tipo do pokemon
            if tipo_pokemon_1 in type_pokemon:
                box_tipo_one["bg"] = type_pokemon[tipo_pokemon_1]
                tipo["bg"] = type_pokemon[tipo_pokemon_1]
                img["bg"] = type_pokemon[tipo_pokemon_1]
            
            tipo_pokemon_2 = f'{pokemon_lista[index]["Tipo_2"]}'
            tipo_secundario["text"] = str(tipo_pokemon_2)

            if tipo_pokemon_2 == "":
                box_tipo_two["bg"] = '#FFFAFA'
                tipo_secundario["bg"] = '#FFFAFA'

            elif tipo_pokemon_2 != "":
        
                if tipo_pokemon_2 in type_pokemon:
                    box_tipo_two["bg"] = type_pokemon[tipo_pokemon_2]
                    tipo_secundario["bg"] = type_pokemon[tipo_pokemon_2]

        # Botão que ao clicar abre o mini jogo   
        def open_game():
            os.system('MiniGame.py')

        game_button = Button(text = "MiniGame", command = open_game)
        game_button.pack()
        game_button.place(x = 400, y = 370)


        layout_superior = Label(root, text = '------- Pokedex -------') #primeira label na interface
        layout_superior.configure(bg = 'red') #cor da label superior
        layout_superior.pack(side = TOP, expand = False, fill = 'x')#posição em relação ao espaço na tela, e quando ela se expande no eixo X

        listagem_pokemon = Listbox(root, selectmode = BROWSE) #div usada para alocar a lista dos nomes e id dos pokemons
        listagem_pokemon.configure(relief = 'groove', border = 3, font = 'Times 12 bold',bg = '#FA8072') #configuraçõa de borda de fonte da div e os elemntos dentro dela
        listagem_pokemon.pack(side = LEFT, expand = False, fill = 'both') #localidade, expansão onde a div foi colocada

        div_1 = Scrollbar() #metodo de barra de rolagem
        div_1.pack(side = RIGHT,fill = 'y') #posição que foi inserido, lado que ficara e posição vertical ou horizontal
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

        box_name = Canvas()
        box_name.pack()
        box_name.configure()
        box_name['width'] = 110
        box_name['height'] = 25
        box_name.place(x = 290, y = 35)

        nome = Label(text = "???????")
        nome.pack()
        nome.configure(font = 'times 14 bold',)
        
        box_name.create_window(55,12, window = nome)

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

        altura = Label(text = "???? m")
        altura.configure(font = 'times 12')
        altura.place(x = 370, y = 170)

        attack = Label(text = "Ataque:")
        attack.configure(font = 'times 12 bold')
        attack.place(x = 175, y = 200)

        ataque = Label(text = "????")
        ataque.configure(font = 'times 12')
        ataque.place(x = 230, y = 200)

        defense = Label(text = "Defesa:")
        defense.configure(font = 'times 12 bold')
        defense.place(x = 175, y = 230)

        defesa = Label(text = "????")
        defesa.configure(font = 'times 12')
        defesa.place(x = 230, y = 230)

        sp_attack = Label(text = "Sp.Ataque:")
        sp_attack.configure(font = 'times 12 bold')
        sp_attack.place(x = 175, y = 260)

        sp_ataque = Label(text = "????")
        sp_ataque.configure(font = 'times 12')
        sp_ataque.place(x = 260, y = 260)

        sp_defense = Label(text = "Sp.Defesa")
        sp_defense.configure(font = 'times 12 bold')
        sp_defense.place(x = 175, y = 290)

        sp_defesa = Label(text = "????")
        sp_defesa.configure(font = 'times 12')
        sp_defesa.place(x = 260, y = 290)

        habitat = Label(text = "Habitat:")
        habitat.configure(font = 'times 12 bold')
        habitat.place(x = 175, y = 380)

        hab = Label(text = "????")
        hab.configure(font = 'times 12')
        hab.place(x = 240, y = 380)

        habilidades = Label(text = "Habilidades:")
        habilidades.configure(font = 'times 12 bold')
        habilidades.place(x = 175, y = 350)

        habilities = Label(text = "????")
        habilities.configure(font = 'times 12')
        habilities.place(x = 260, y = 350)

        speed = Label(text = "Velocidade")
        speed.configure(font = 'times 12 bold')
        speed.place(x = 175, y = 320)

        velocidade = Label(text = "????")
        velocidade.configure(font = 'times 12')
        velocidade.place(x = 260, y = 320)


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
root.resizable(0,0)
Application(root)
root.mainloop() # mantém a interface ligada rodando o codigo, que só fechado quando precionado o botão fechar