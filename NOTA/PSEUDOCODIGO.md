NOTA(PSEUDOCODIGO)

INICIO
    DEFINIR total_das_notas = 0
    DEFINIR contador_alunos = 0

    ENQUANTO (contador_alunos < 5)
        ESCREVER "Digite a nota do aluno ", contador_alunos + 1
        LER nota

        // Laço de validação //
        ENQUANTO (nota < 0 OU nota > 10)
            ESCREVER "Nota invalida. Digite novamente."
            LER nota
        FIM ENQUANTO

        // Acumula a nota válida e conta o aluno //
        total_das_notas = total_das_notas + nota
        contador_alunos = contador_alunos + 1
    FIM ENQUANTO

    media = total_das_notas / 5
    ESCREVER "A media das notas é: " + media
FIM