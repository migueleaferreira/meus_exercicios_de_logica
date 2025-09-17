# LISTA DE COMPRAS

# Crie um programa que ajude o usuário a montar uma lista de compras.
# O seu programa deve:
# Começar com uma lista de compras vazia.
# Pedir ao usuário para digitar um item de cada vez.
# Adicionar o item que ele digitou à lista.
# Continuar pedindo itens até que o usuário digite a palavra 'fim'.
# Depois que o usuário digitar 'fim', o programa deve mostrar a lista de compras completa.

# Dica: Você pode usar um laço while que roda para sempre (while True:).
# Para parar o laço, use uma condição com if e o comando break quando o usuário digitar 'fim'.


listaCompra = []

print("---LISTA DE COMPRAS--")
print("--Digite FIM para encerrar a lista de compras--")

while True:
    compra = input("Digite o item para compra: ")

    if not compra:
        print("Digite algo valido")
        continue
    
    if compra.lower() == "fim":
        encerrar = input("deseja encerrar?(sim/Não) ")
            
        if encerrar.lower() == "sim":
                break
        elif encerrar.lower() == "não":
                continue

    listaCompra.append(compra)

print("\nSua lista de compras")
print(listaCompra)