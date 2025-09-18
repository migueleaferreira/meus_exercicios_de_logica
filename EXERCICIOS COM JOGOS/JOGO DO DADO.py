# JOGO DE DADO

# Vamos criar um pequeno jogo onde o computador "joga um dado" 
# e você tenta adivinhar o número.

# Seu programa deve:
# Gerar um número aleatório entre 1 e 6 (como em um dado).
# Perguntar ao usuário para adivinhar o número.
# Usar if, elif e else para dizer ao usuário se ele acertou ou não.
# No final, mostre qual era o número correto.

import random
random_adivinha = random.randint(1, 6)

print("---JOGO DO DADO---")
print("--Digite um numero entre 1 a 6--")

while True:
    adivinha = int(input("Chute um numero: "))

    if adivinha == random_adivinha:
        print("Parabens você acertou!!")
        print(f"O numero era {random_adivinha}")
        break
    elif adivinha > 6:
       continue
    else:
        print("Tente novamente")

