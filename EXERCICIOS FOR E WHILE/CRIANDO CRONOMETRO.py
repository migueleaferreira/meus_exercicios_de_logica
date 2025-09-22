# CRIANDO CRONOMETRO
# A ideia é fazer um programa que conta de 5 até 1 e depois diz "Go!".

# Use um laço for para contar de 5 até 1 fazer um range que conta de trás para frente!).
# Dentro do laço, imprima o número.
# Embaixo de cada print, coloque a linha time.sleep(1) para fazer o seu programa esperar um segundo.
# Depois que o laço terminar, imprima a mensagem "Go!".

import time 

num = int(input("Qual o nemero deseja para a contagem regressiva?: "))

for i in reversed(range(1, num + 1)):
    print(f"{i}")
    time.sleep(1)
print("GO!")