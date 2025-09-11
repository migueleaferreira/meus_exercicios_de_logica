# SOMAR NUMEROS PARES

# Faça um programa que peça ao usuário para digitar um número inteiro.
# Em seguida, seu programa deve somar todos os números pares de 1 até o número que o usuário digitou.

# Exemplo:
# Se o usuário digitar 10, a soma deve ser 2 + 4 + 6 + 8 + 10, que é igual a 30.

# Dica: Você vai precisar de um laço for. 
# Para checar se um número é par, você pode usar o operador de módulo (%). 
# O operador % retorna o resto de uma divisão. Se numero % 2 for igual a 0, o número é par.

somar = 0
numero = int(input("Digite um numero inteiro: "))

pares = [] 

for numeros in range(1, numero + 1):
    if numeros % 2 == 0:
        somar += numero
        pares.append(numeros)  

print(f"A soma de {pares} é {somar}")
