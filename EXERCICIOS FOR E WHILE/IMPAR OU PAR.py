# IMPAR OU PAR

# Faça um programa que use um laço de repetição for para exibir os números de 1 a 20. Para cada número, diga se ele é par ou ímpar.

for i in range (1,21):
    if i % 2 == 0:
        print(f"esse numero {i} é par")
    else:
        print(f"esse numero {i} é impar")