FAZER CAFÉ: (PSEUDOCÓDIGO)

INÍCIO
  pegar_materiais(pó_café, água, bule, suporte, filtro, colher, xícara, açúcar_opcional)
  medir_e_colocar_água_no_bule(qtd_água)
  SE fogão_desligado ENTÃO ligar_fogão
  colocar_bule_no_fogo
  ENQUANTO NÃO água_ferveu FAÇA
      aguardar
  FIMENQUANTO
  desligar_fogão
  colocar_filtro_no_suporte
  adicionar_pó_no_filtro(qtd_pó)
  ENQUANTO água_restante > 0 FAÇA
      despejar_água_quente_lentamente()
      esperar_escorrer()
  FIMENQUANTO
  servir_café_na_xícara
  SE quer_açúcar ENTÃO
      adicionar_açúcar(qtd)
      mexer()
  FIMSE
  descartar_filtro
  lavar_utensílios
FIM