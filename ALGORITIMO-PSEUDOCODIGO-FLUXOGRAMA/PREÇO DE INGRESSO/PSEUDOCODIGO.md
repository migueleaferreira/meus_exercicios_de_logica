PREÇO DO INGRESSO(PSEUDOCODIGO)

INICIO
  LER idade_do_ingresso

  SE (idade_do_ingresso <= 16) ENTAO
    ESCREVER "Criança: você paga meia."
  SENÃO SE (idade_do_ingresso >= 17 E idade_do_ingresso <= 59) ENTAO
    ESCREVER "Adulto: você paga inteira."
  SENAO
    ESCREVER "Idoso: você paga meia."
FIM
