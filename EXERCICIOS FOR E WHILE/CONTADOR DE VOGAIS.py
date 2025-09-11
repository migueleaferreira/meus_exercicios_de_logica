# CONTADOR DE VOGAIS

# Faça um programa que peça ao usuário para digitar uma frase. 
# Conte e exiba o número de vogais (a, e, i, o, u) que existem na frase.

vogais_encontradas = set() #Um conjunto que não permite repetições. Quando você adiciona um item que já está lá, ele é ignorado
contador = 0
vogal = input("Digite uma frase: ")

for letra in vogal:
    

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1
        vogais_encontradas.add(letra)
        

print(f"suas vogais são: {contador}, e são {vogais_encontradas}") #a ',' é pq não pode juntar int con string com '+' 
   

