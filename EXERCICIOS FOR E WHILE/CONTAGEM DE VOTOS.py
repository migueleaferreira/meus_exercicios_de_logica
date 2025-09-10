# CONTAGEM DE VOTOS

# Faça um programa que use um laço de repetição for para pedir a nota de 10 produtos, 
# de 1 a 5, para o usuário.
# No final, exiba:
# A quantidade de votos para cada nota (quantos produtos receberam nota 1, quantos receberam nota 2, etc.).
# A média geral de todas as notas.

# Dica:
# Você pode usar uma lista ou variáveis separadas para contar os votos de cada nota.
# Use uma estrutura de decisão (if/else) para verificar a nota digitada e somar o voto no lugar certo.
# O for deve rodar 10 vezes.

votos_1 = 0
votos_2 = 0
votos_3 = 0
votos_4 = 0
votos_5 = 0
somar_votos = 0

for notas in range(1,11):
    produto = int(input("digite a nota : "))
    
    somar_votos = somar_votos + produto

    

    if produto == 1:
        votos_1 += 1
    elif produto == 2:
        votos_2 += 1
    elif produto == 3:
        votos_3 += 1
    elif produto == 4:
        votos_4 += 1
    elif produto == 5:
        votos_5 += 1

media = somar_votos / 10
print(votos_1)
print(votos_2)
print(votos_3)
print(votos_4)
print(votos_5)
print(media)

