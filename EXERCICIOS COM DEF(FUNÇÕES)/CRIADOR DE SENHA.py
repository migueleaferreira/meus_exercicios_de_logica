# CRIADOR DE SENHA

# Antes de tudo, você vai precisar do módulo random (para fazer escolhas aleatórias) 
# e de uma lista de "ingredientes" para sua senha.

# A Função: Crie a estrutura básica da função: def gerar_senha(tamanho):.

# Os Caracteres: Crie uma variável que contém todos os caracteres possíveis 
# (letras minúsculas e maiúsculas, e números).

# Sua primeira tarefa é essa: Crie a função e a variável de caracteres. 
# Por exemplo, você pode começar só com letras minúsculas e números.

import random
import string

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
senha = ""
todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros

def gerar_senha(tamanho):
    senha = ""
    for i in range(tamanho):
        aleatoria = random.choice (todos_os_caracteres)
        senha += aleatoria
        
    return senha
    
tamanho_desejado = int(input("Qual o tamanho da senha que você deseja?: "))
minha_nova_senha = gerar_senha(tamanho_desejado)
print(f"Sua nova senha é: {minha_nova_senha}")


















