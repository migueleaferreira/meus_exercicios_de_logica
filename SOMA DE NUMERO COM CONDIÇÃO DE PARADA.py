# SOMA DE NUMERO COM CONDIÇÃO DE PARADA

# Faça um programa que peça ao usuário para digitar números. 
# O programa deve continuar pedindo números até que o usuário digite o número zero. 
# No final, exiba a soma de todos os números digitados.

# Dica:
# Use um laço while para que o programa continue pedindo números.
# A condição do seu while deve ser enquanto o número for diferente de zero.
# Você vai precisar de uma variável para somar os números. Lembre-se de criá-la antes do while.

somar_numeoros = 0


numero = int(input("Digite um numero: "))

somar_numeoros = somar_numeoros + numero


while numero != 0:
    numero = int(input("Digite um outro numero: "))

    somar_numeoros = somar_numeoros + numero

    if numero == 0:
        print("acertou o numero,", end=" ")
    else:
        print("tente novamente")

print("a soma de todos numeros são ", somar_numeoros)


   

