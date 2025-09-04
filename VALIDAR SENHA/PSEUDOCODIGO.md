VALIDAR SENHA(PSEUDOCODIGO)

  DEFINIR senha_correta = 123
  DEFINIR tentativas = 0
  DEFINIR senha_digitada = NULO

  ENQUANTO (senha_digitada != senha_correta E tentativas < 3)
    LER senha_digitada
    SE (senha_digitada == senha_correta) ENTAO
      ESCREVER "Senha correta, acesso liberado."
    SENÃO
      ESCREVER "Senha incorreta. Tente novamente."
    FIM SE
    tentativas = tentativas + 1
  FIM ENQUANTO

  SE (senha_digitada != senha_correta) ENTAO
    ESCREVER "Você excedeu o número de tentativas. Tente novamente em 30 minutos."
  FIM SE
FIM