# CATALOGO DE PRODUTOS(FOCO EM DICIONARIO (CRUD))

import json
import os

catalogo_produtos = {}


def registrar_produtos(nome, preco, quantidade):

    detalhes = {"preco": preco, "quantidade": quantidade}

    # usando o "nome" como chave principal
    catalogo_produtos[nome] = detalhes
    print(f"Produto '{nome}' registrado com sucesso!")


# 3. FUNÇÃO READ (Consulta de Produto)
def consultar_produto(nome_busca):

    if nome_busca in catalogo_produtos:
        produto = catalogo_produtos[nome_busca]

        print("\n--- DETALHES DO PRODUTO ---")
        print(f"Nome: {nome_busca}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Estoque: {produto['quantidade']} unidades")
    else:
        # Se não existir, informa o erro
        print(f"\nErro: Produto '{nome_busca}' não encontrado no catálogo.")


# DESAFIO 1: ATUALIZAÇÃO (UPDATE) DO CATALOGO
def atualizar_produto(nome, novo_preco, nova_quantidade):

    if nome in catalogo_produtos:

        catalogo_produtos[nome]['preco'] = novo_preco
        catalogo_produtos[nome]['quantidade'] = nova_quantidade

        print(f"\n Produto '{nome}' atualizado com sucesso!")

    else:
        print(
            f"\n Erro de Atualização: Produto '{nome}' não encontrado para modificação.")


# DESAFIO 2: EXCLUIR
def excluir_produto(nome):
    if nome in catalogo_produtos:
        del catalogo_produtos[nome]


# DESAFIO 3: SALVANDO DADOS (CONTINUAÇÃO)
def salvar_dados():
    with open("CATALOGO DE PRODUTOS.json", "w") as arquivo_saida:
        # dump (Salvar)	Precisa da origem e do destino.
        json.dump(catalogo_produtos, arquivo_saida)


# DESAFIO 4: CARREGAMENTO DE DADOS
def carregar_dados():
    global catalogo_produtos
    if os.path.exists("CATALOGO DE PRODUTOS.json"):
        with open("CATALOGO DE PRODUTOS.json", "r") as arquivo:
            # load (Carregar) Precisa da origem e devolve o resultado.
            catalogo_produtos = json.load(arquivo)


# DESAFIO 4: INTEGRAÇÃO FINAL (MENU)
def menu_principal():
    while True:
        print("1: para Registrar, \n2: para Consultar, \n3: para Atualizar, \n4: Para Excluir, \n5: Para Sair")
        escolha = input("Qual opção deseja? ")

        if escolha == "1":
            pedir_produto = input("Qual produto deseja adicionar? ")
            pedir_preco = int(input("Qual o preço? "))
            pedir_quantidade = int(input("Quantas quantidade? "))
            registrar_produtos(pedir_produto, pedir_preco, pedir_quantidade)
            salvar_dados()

        elif escolha == "2":
            consultar_produto1 = input("Qual deseja consultar? ")
            consultar_produto(consultar_produto1)

        elif escolha == "3":
            atualizar_produto1 = input("Qual produto deseja adicionar? ")
            atualizar_preco = int(input("Qual o preço? "))
            atualizar_quantidade = int(input("Quantas quantidade? "))
            atualizar_produto(atualizar_produto1, atualizar_preco, atualizar_quantidade)
            salvar_dados()

        elif escolha == "4":
            excluir_produto1 = input("Qual deseja excluir? ")
            excluir_produto(excluir_produto1)
            salvar_dados()

        elif escolha == "5":
            salvar_dados()
            break
        
        else:
            print("Escolha uma opção valida")


if __name__ == "__main__":
    carregar_dados()  # 1. Traz os dados salvos
    menu_principal()  # 2. Inicia a interação
