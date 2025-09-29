# GERENCIADOR DE COMPRAS

lista_de_compras = []


def adicionar_item(item):
    lista_de_compras.append(item)
    print(f" {item} foi adicionado na sua lista")


def remover_item(item):
    try:
        lista_de_compras.remove(item)
        print(f"{item} foi removido")
    except ValueError:
        print("Error")
        print(f"Erro: '{item}' não está na lista. Nenhum item foi removido.")


def mostrar_lista():
    if not lista_de_compras:
        print("A lista de compras está vazia.")
        return
        
    print("\n--- SUA LISTA DE COMPRAS ---")
    for i, item in enumerate(lista_de_compras, 1):
        print(f"{i}. {item}")
    print("----------------------------\n")


        

while True:
    print("1: Adicionar \n2: Remover \n3: Mostrar \n4: Sair")
    escolha = input("Qual opção você deseja?: ")
    if escolha == "1":
        novo_item = input("Qual item deseja adicionar? ")
        adicionar_item(novo_item)
        

    elif escolha == "2":
         excluir = input("Qual item deseja excluir? ")
         remover_item(excluir)
         

    elif escolha == "3":
        mostrar_lista() 

    elif escolha == "4":
        print("Sessão encerrada!")
        break

    else:
        print("Opção invalida")

        




