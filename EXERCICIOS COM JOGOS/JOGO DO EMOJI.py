# JOGO DO EMOJI

# Seu programa vai precisar de uma lista de emojis e suas respostas para funcionar.
# O dicionário é perfeito para isso!

# O seu jogo deve ter a seguinte lógica:
# Crie um dicionário com os emojis como chaves e os nomes dos filmes/séries como valores.
# (Exemplo: {"👻➡️👨‍👦": "Os Caça-Fantasmas"}).
# Use a biblioteca random para escolher uma chave aleatória (um emoji) desse dicionário.
# Mostre o emoji na tela e peça ao usuário para tentar adivinhar qual é o filme/série.
# Use um if/else para checar se o chute do usuário é igual ao valor correspondente no dicionário.
# Avise se o usuário acertou ou errou.

soma = 0
pontos_facil = 0
pontos_medio = 0
pontos_dificil = 0

emoji_facil = {
    "🧙‍♂️⚡️🏰": "Harry Potter",
    "➡️🚗💨": "Velozes e Furiosos",
    "🦁👑➡️🌳": "O Rei Leão",
    "🦸‍♂️🛡️🇺🇸": "Capitão América",
    "🦇🌃🤵": "Batman",
    "🧊🛳️💔": "Titanic",
    "🕷️🧑‍🦱": "Homem Aranha",
    "👸🏻❄️☃️": "Frozen",
    "🧟‍♂️🔫🌍": "Resident Evil",
    "🐠🔍🌊": "Procurando Nemo",
}

emoji_medio = {
    "💊🔴🔵": "Matrix",
    "🤡🎈🔪": "It A Coisa",
    "🕰️🧑🏻‍🚀🪐🌌": "Interestelar",
    "👨🏻‍💼🤵🏻‍♂️🔫💥": "O Poderoso Chefão",
    "🦕🌋🏃🏻": "Jurassic Park",
    "👨🏻‍🚀🌕🇺🇸": "Apollo 13",
    "👩🏻‍🚀🚀🌌": "Gravidade",
    "🦸‍♂️🧤💎": "Vingadores Ultimato",
    "🛸👽☎️": "ET O Extraterrestre",
    "👦🏻🐉🐉": "Como Treinar o Seu Dragão",
}

emoji_dificil = {
    "👦🏻🏠🎄😡": "Esqueceram de Mim",
    "🤫🌳🏡👽": "Um Lugar Silencioso",
    "⚛️💥🧑🏻‍🔬": "Oppenheimer",
    "🧑🏻🪞🌌": "A Origem",
    "🔪🚿🚪": "Psicose",
    "👩🏻‍🦰🧑🏻‍🦰🎭": "Clube da Luta",
    "🧑🏻‍🚀🤖🌌": "2001 Uma Odisseia no Espaço",
    "🐰⌛🔄": "Donnie Darko",
    "🧑🏻‍🎤⚡👨🏻‍🎤": "Bohemian Rhapsody",
    "🚢🦑🌊": "20.000 Léguas Submarinas",
}


lista_de_emoji_facil = list(emoji_facil.keys())
lista_de_emoji_medio = list(emoji_medio.keys())
lista_de_emoji_dificil = list(emoji_dificil.keys())

  
nome = input("Digite o seu nome: ")
print(f"--Bem vindo {nome}, tente adivinhar os filmes por emoji--")
escolha = input("Qual modo você vai querer? Facil, Medio ou dificil?: ") 

if escolha.lower() == "facil".lower():
    for lista_da_vez1 in lista_de_emoji_facil:
        for tentativas in range(3):
            print(f"{lista_da_vez1}")
            chute = input("Qual é o filme: ")

            if chute.lower() == emoji_facil[lista_da_vez1].lower():
                print("Você acertou!\n")
                pontos_facil += 1
                break
            else:
                print("Você errou!\n")
                
                
                soma = soma + pontos_facil
    print(f"Você acertou {pontos_facil} de {len(lista_de_emoji_facil)} filmes no modo fácil.")

if escolha.lower() == "Medio".lower():
    for lista_da_vez2 in lista_de_emoji_medio:
        for tentativas in range(3):
            print(f"{lista_da_vez2}")
            chute2 = input("qual é o filme: ")

            if chute2.lower() == emoji_medio[lista_da_vez2].lower():
                print("Você acertou!\n")
                pontos_medio += 1
                break
            else:
                print("Você errou!\n")
                break
            soma = soma + pontos_medio

    print(f"Você acertou {pontos_medio} de {len(lista_de_emoji_medio)} filmes no modo medio.")
        
if escolha.lower() == "Dificil".lower():
    for lista_da_vez3 in lista_de_emoji_dificil:
        for tentativas in range(3):
            print(f"{lista_da_vez3}")
            chute3 = input("Qual é o filme: ")

            if chute3.lower() == emoji_dificil[lista_da_vez3].lower():
                print("Você acertou!\n")
                pontos_dificil += 1 
                break
            else:
                print("Você errou!\n")
                break
            soma = soma + pontos_dificil

    print(f"Você acertou {pontos_dificil} de {len(lista_de_emoji_dificil)} filmes no modo dificil.")