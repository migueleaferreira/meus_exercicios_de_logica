# VALIDADOR DE SENHA

# Faça um programa que peça ao usuário para criar uma senha. A senha deve ter as seguintes regras:
# Ter pelo menos 8 caracteres.
# Conter pelo menos uma letra maiúscula.
# Conter pelo menos um número.
# O seu programa deve continuar pedindo uma nova senha até que o usuário crie uma que atenda a todas as três regras.
# Depois, exiba uma mensagem de sucesso.

# Dica: Pense em como você pode verificar o comprimento da senha e se ela contém letras maiúsculas ou números.

print("-----> senha deve ter pelo menos 8 caracteres entre eles numeros e uma letra maiuscula. ex: Senha123 <-----")

while True:
    senha = input("Crie sua senha: ")

    tem_tamanho = (len(senha) >= 8)
    tem_maiuscula = False
    tem_numero = False

    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        if letra.isdigit():
            tem_numero = True

    if tem_tamanho and tem_maiuscula and tem_numero:
        print("Senha criada com sucesso!")
        break
    else:
        print("Senha inválida. Tente novamente.")
        print("Sua senha precisa ter:")
        if not tem_tamanho:
            print("- Pelo menos 8 caracteres")
        if not tem_maiuscula:
            print("- Pelo menos uma letra maiúscula")
        if not tem_numero:
            print("- Pelo menos um número")
    print() 


