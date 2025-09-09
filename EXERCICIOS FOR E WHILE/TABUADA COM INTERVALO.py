# TABUADA COM INTERVALO

# Escreva um programa que peça ao usuário um número e o limite da tabuada. 
# Em seguida, exiba a tabuada desse número. Se o limite for maior que 20, exiba uma mensagem de aviso e não exiba a tabuada.

# Passo a passo da lógica(algoritimo):

# Peça ao usuário para digitar o número da tabuada.

# Peça ao usuário para digitar o limite.

# Use uma estrutura de decisão (se) para verificar se o limite é maior que 20.

# Se o limite for maior que 20, imprima a mensagem de erro.

# Se o limite não for maior que 20, use um laço de repetição (para ou enquanto) para calcular e exibir a tabuada.

tabuada = int(input("Digite o numero da tabuada: "))
limite = int(input("digite o limite: "))

if (limite >20):
    print("ERROR, O LIMITE É 20")
else:
    for i in range(1,limite + 1):
        res = tabuada * i
        print(res)

