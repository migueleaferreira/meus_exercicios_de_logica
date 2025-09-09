SINAL DE TRANSITO(PSEUDOCODIGO)

INICIO
  LER cor_do_semaforo

  SE (cor_do_semaforo == "verde") ENTAO
    ESCREVER "Siguir"
  SENÃO SE (cor_do_semaforo == "amarelo") ENTAO
    ESCREVER "Atenção"
  SENÃO SE (cor_do_semaforo == "vermelho") ENTAO
    ESCREVER "Parar"
  SENAO
    ESCREVER "Cor inválida. Verifique o semáforo."
FIM

