# JOGO DO EMOJI

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


def jogar_nivel(dicionario_emojis):
    pontos_atuais = 0 

    lista_de_emojis_do_nivel = list(dicionario_emojis.keys())

    for emoji_da_vez in lista_de_emojis_do_nivel:
        for tentativas in range(3):
            print(f"{emoji_da_vez}")
            chute = input("Qual é o filme: ")

            if chute.lower() == dicionario_emojis[emoji_da_vez].lower():
                print("Você acertou!\n")
                pontos_atuais += 1
                break
            else:
                print("Você errou!\n")
    print(f"Você acertou {pontos_atuais} de {len(lista_de_emojis_do_nivel)} filmes.")

nome = input("Digite o seu nome: ")
print(f"--Bem vindo {nome}, tente adivinhar os filmes por emoji--")
escolha = input("Qual modo você vai querer? Facil, Medio ou dificil?: ")

if escolha.lower() == "facil":
    jogar_nivel(emoji_facil)
elif escolha.lower() == "medio":
    jogar_nivel(emoji_medio)
else:
    jogar_nivel(emoji_dificil)