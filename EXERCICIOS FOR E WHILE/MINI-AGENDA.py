# MINI-AGENDA

# Crie um programa que funcione como uma agenda de contatos simples.
# Seu programa deve:

# Começar com um dicionário vazio para a agenda.
# Perguntar o nome de uma pessoa.
# Perguntar o número de telefone dessa pessoa.
# Adicionar o nome e o número na sua agenda.
# Repetir os passos 2, 3 e 4 para uma segunda pessoa.
# No final, mostre a agenda completa na tela.

# Dica: Você pode criar um dicionário vazio com agenda = {}. 
# Para adicionar um novo contato, use a sintaxe agenda[nome] = numero.

agenda = {}

agendaNome = input("Digite o nome: ")
agendaNumero = int(input("\nDigite o numero: "))

agenda[agendaNome] = agendaNumero

print(agenda)