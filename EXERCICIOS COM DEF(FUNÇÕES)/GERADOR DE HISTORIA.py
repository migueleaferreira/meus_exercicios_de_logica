# GERADOR DE HISTORIA

import random

gerar_lugares = ["São Paulo", "Rio de Janeiro", "Minas Gerais"]
gerar_adjetivos = ["legal", "gentil", "inteligente"]
gerar_personagens = ["Ana", "Marcos", "Ariel"]


def gerar_historia():
    lugar_escolhido = random.choice(gerar_lugares)
    adjetivo_escolhido = random.choice(gerar_adjetivos)
    personagens_escolhido = random.choice(gerar_personagens)

    print(f"Eu estava em {lugar_escolhido}, quando derrepente apareceu uma pessoa {adjetivo_escolhido}. Foi ai que soube que era o amor da minha vida, e seu nome era {personagens_escolhido}")

    return 


print(gerar_historia())
