# CALCULADORA DE MEDIA

# Crie um programa que calcula a média de notas de um aluno.

# O seu programa deve:
# Perguntar ao usuário quantas notas ele quer calcular.
# Usar um laço for para pedir ao usuário para digitar cada uma das notas, uma por vez.
# Somar as notas à medida que elas são digitadas.
# Depois que o laço terminar, calcular a média das notas.
# Mostrar na tela a média final.

soma = 0
mediaFinal = 0

nota = int(input("quantas notas voce quer calcular? "))

for notas in range(nota):
    media = float(input("Digite a nota: "))
    soma = soma + media 

mediaFinal = soma / nota

print(f"Sua media é {mediaFinal}")

if mediaFinal >=7:
    print("Você passou")
else:
    print("Você não passou")
    