MENU DE OPERAÇÃO(PSEUDOCODIGO)

INICIO
  DEFINIR opcao_menu = 0
  DEFINIR n1, n2, resultado

  ENQUANTO (opcao_menu != 4)
    ESCREVER "--- MENU DE OPERACOES ---"
    ESCREVER "1. Somar"
    ESCREVER "2. Subtrair"
    ESCREVER "3. Multiplicar"
    ESCREVER "4. Sair"
    ESCREVER "Escolha uma opcao: "
    LER opcao_menu

    SE (opcao_menu >= 1 E opcao_menu <= 3)
      ESCREVER "Digite o primeiro numero: "
      LER n1
      ESCREVER "Digite o segundo numero: "
      LER n2

      ESCOLHA (opcao_menu)
        CASO 1:
          resultado = n1 + n2
          ESCREVER "O resultado da soma eh: ", resultado
          PARE

        CASO 2:
          resultado = n1 - n2
          ESCREVER "O resultado da subtracao eh: ", resultado
          PARE

        CASO 3:
          resultado = n1 * n2
          ESCREVER "O resultado da multiplicacao eh: ", resultado
          PARE
      FIM ESCOLHA
    SENAO SE (opcao_menu != 4)
        ESCREVER "Opcao invalida. Por favor, escolha uma opcao entre 1 e 4."
    FIM SE
  FIM ENQUANTO

  ESCREVER "Programa finalizado."
FIM