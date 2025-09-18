# CALCULADORA DE IDADE

# Crie um programa que:
# Pergunte ao usuário em que ano ele nasceu.
# Calcule a idade dele.
# Mostre na tela a idade.


soma = 0
anoAtual = 2025

idade = int(input("Em que ano você nasceu? :"))

if idade > anoAtual:
    print("Digite o ano atual!")
else:
    soma = (anoAtual - idade)
    print(f"Você tem {soma} anos")

