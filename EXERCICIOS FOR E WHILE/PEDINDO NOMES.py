# PEDINDO NOMES

# Faça um programa que use um laço de repetição for para pedir ao usuário o nome de 3 pessoas. 
# No final, exiba todos os nomes que foram digitados.

# Dica: Para este exercício, você vai precisar de uma lista para guardar os nomes. 
# Você pode criar uma lista vazia no começo do programa e usar o método .append() para 
# adicionar os nomes a ela a cada repetição do laço.

pessoas = []


for nome in range(3):

    nomes = input("digite o nome de uma pessoa: ")
    pessoas.append(nomes)
    
print(pessoas)



    





