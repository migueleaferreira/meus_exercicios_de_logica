# MÉDIA E CONDIÇÃO
# Faça um programa que use um laço de repetição while para pedir ao usuário a nota de quatro alunos. 
# No final, exiba a média das notas e uma mensagem dizendo se a média está acima ou abaixo de 7.0.

# Dica:
# Você vai precisar de uma variável de controle para o while 
# (lembre-se de que ela precisa mudar a cada repetição).
# Você vai precisar de uma variável para somar todas as notas.
# Use uma estrutura de decisão (if/else) para verificar se a média é maior ou menor que 7.0

num = 0
somar_notas = 0

while num <4:
    num +=1

    nota_do_aluno = int(input("digite a nota do aluno: "))

    somar_notas = somar_notas + nota_do_aluno
    
media = somar_notas / 4
    
if media >=7:
        print("Parabens! você esta acima da média")
else:
        print("Você esta abaixo da média")
