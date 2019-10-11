pokemon_lista = [ 
{'ID' : 1, 
'Nome' : "Bulbasauro", 'Tipo' : "Planta/Venenoso", 
'Peso' :  6.9, 'Altura' : 0.7, 
'Descricao' : "Pokemon Semente",
'Info' : "Por algum tempo após seu nascimento, cresce  ao se alimentar das sementes nas costas" },

{'ID' : 2, 
'Nome' : "Ivysauro", 'Tipo' : "Planta/Venenoso", 
'Peso' :  13, 'Altura' : 1, 
'Descricao' : "Pokemon Semente",
'Info' : "Quando o botão nas costas começa a inchar, um aroma doce flutua para indicar as flores que florescem" },

{'ID' : 3, 
'Nome' : "Venasauro", 'Tipo' : "Planta/Venenoso", 
'Peso' :  100, 'Altura' : 2, 
'Descricao' : "Pokemon Semente",
'Info' : "Após um dia chuvoso, a flor nas costas cheira mais forte. O perfume atrai outros Pokémon" },

{'ID' : 4, 
'Nome' : "Charmander", 'Tipo' : "Fogo", 
'Peso' :  8.5, 'Altura' : 0.6, 
'Descricao' : "Pokemon Lagarto",
'Info' : "O fogo na ponta da cauda é uma medida da sua vida. Se saudável, sua cauda queima intensamente"},

{'ID' : 5, 
'Nome' : "Charmeleon", 'Tipo' : "Fogo", 
'Peso' :  19, 'Altura' : 1.1, 
'Descricao' : "Pokemon Chamas",
'Info' : "Nas montanhas rochosas onde Charmeleon vive, suas caudas ardentes brilham à noite como estrelas" },

{'ID' : 6, 
'Nome' : "Charizard", 'Tipo' : "Fogo/Voador", 
'Peso' :  90.5, 'Altura': 1.7 , 
'Descricao' : "Pokemon Chamas",
'Info' : "Dizem que o fogo dos Charizards queima mais quente se tiver passado por batalhas duras" },

{'ID' : 7, 
'Nome' : "Squirtle", 'Tipo' : "Água", 
'Peso' :  9, 'Altura': 0.5 , 
'Descricao' : "Pokemon Tartaura-jovem",
'Info' : "Ele se abriga em sua concha e depois revida com bicos de água a cada oportunidade"},

{'ID' : 8, 
'Nome' : "Wartortle", 'Tipo' : "Água", 
'Peso' :  22.5, 'Altura': 1 , 
'Descricao' : "Pokemon tartaruga",
'Info' : "Diz-se que vive 10.000 anos.Sua cauda peluda é popular como um símbolo da longevidade" },

{'ID' : 9, 
'Nome' : "Blastoise", 'Tipo' : "Água", 
'Peso' :  85.5, 'Altura': 1.6 , 
'Descricao' : "Pokemon Concha",
'Nome' : "Caterpie", 'Tipo' : "Inseto", 
'Peso' :  2.9, 'Altura': 0.3 , 
'Descricao' : "Pokemon Lagarta",
'Info' : "Ele libera um fedor de sua antena vermelha para repelir os inimigos. Cresce mudando repetidamente" },

{'ID' : 11, 
'Nome' : "Metapode", 'Tipo' : "Inseto", 
'Peso' :  9.9, 'Altura': 0.7 , 
'Descricao' : "Pokemon Crisálida",
'Info' : "Uma concha de aço duro protege seu corpo sensível. Ele silenciosamente suporta dificuldades enquanto aguarda a evolução" },

{'ID' : 12,
'Nome' : "Butterfree", 'Tipo' : "Inseto/Voador",
'Peso' : 32, 'Altura' : 1.1,
'Descricao' : "Pokemon Borboleta",
'Info' : "Ele Adora o mel das flores e pode localizar manchas de flores que possuem quantidades minúsculas de pólen"},

{'ID' : 13,
'Nome' : "Weedle", 'Tipo' : "Inseto/Venenoso",
'Peso' : 3.2, 'Altura' : 0.3,
'Descricao' : "Pokemon Lagarta Peluda",
'Info' : 'Come seu peso nas folhas todos os dias. Afasta os atacantes com a agulha na cabeça'},

{'ID' : 14,
'Nome' : "Kakuna", 'Tipo' : "Inseto/Venenoso",
'Peso' : 10, 'Altura' : 0.6,
'Descricao' : "Pokemon Pupa",
'Info' : "Enquanto aguarda a evolução, esconde-se de predadores sob folhas e em recantos de galhos"},

{'ID' : 15,
'Nome' : "Beedrill", 'Tipo' : "Inseto/Venenoso",
'Peso' : 29.5, 'Altura' : 1,
'Descricao' : "Pokemon Abelha venenosa",
'Info' : "Seu melhor ataque envolve voar em alta velocidade, golpear com agulhas de veneno e depois voar"}

]

for id_pokemon, pokemon in enumerate(pokemon_lista):
    print(f'#{id_pokemon:0>3} - {pokemon["Nome"]}')
