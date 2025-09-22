# PALAVRA SECRETA 

# O computador tem uma palavra secreta, e o jogador tem que adivinhar a palavra

# Vamos construir a lógica passo a passo:

# A Palavra Secreta e as Tentativas: Crie duas variáveis. 
# Uma para a palavra secreta (ex: palavra = "python") e outra para o número de tentativas (ex: tentativas = 3).
# O Laço while: Use um laço while que continue rodando enquanto o número de tentativas for maior que 0.
# A Pergunta: Dentro do laço, use input() para pedir ao jogador que ele chute uma letra.
# A Lógica: Use um if/else para checar se a letra que o jogador chutou está na palavra secreta. 
# Você pode fazer isso com a palavra-chave in.



letras_acertadas = ""
palavra = "python"
tentativas = 10

while tentativas > 0:
    chute = input("Adivinhe a letra: ")
    palavra_escondida = ""

   
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_escondida += letra
        else:
            palavra_escondida += "_"

    print("Palavra: ", palavra_escondida)
    
    # Esta é a lógica de acerto e erro
    if chute in palavra:
        print("Letra correta!")
        letras_acertadas += chute  
    else:
        print("Letra incorreta.")
        tentativas -= 1
        print(f"Você tem {tentativas} tentativas restantes.")
        
    # Esta é a lógica de vitória
    if palavra_escondida == palavra:
        print("Parabéns, você acertou a palavra!")
        break

# Esta é a lógica de derrota (fora do laço)
if tentativas == 0:
    print("Suas tentativas acabaram! A palavra era:", palavra)

        
    