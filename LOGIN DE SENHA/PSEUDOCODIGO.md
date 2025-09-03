LOGIN DE SITE (PSEUDOCÓDIGO)

INICIO
 entrar_no_site()
    SE nao_tiver_conta ENTÃO
        criar_conta()
    SENÃO
        entrar()
    FIMSE
    digitar_usuario()
    digitar_senha()
    ENQUANTO usuario_ou_senha_incorretos FAÇA
        mostrar_mensagem("Usuário ou senha incorretos, tente novamente")
        digitar_usuario()
        digitar_senha()
    FIMENQUANTO

    entrar()
FIM