ATRAVESSAR A RUA: (PSEUDOCÓDIGO)

INICIO
olhar_o_sinal
ENQUANTO sinal NÃO for verde FAÇA
    aguardar()
FIMENQUANTO
olhar_para_os_lados()
SE não_tiver_vindo_carro 
    atravessar_a_rua()
SENÃO 
    esperar_o_carro_passar()
    voltar_ao_passo_dois
FIMSE
FIM