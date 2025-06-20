from conexaobd import *
from operacoesbd import listarBancoDados, encerrarConexao

def verManifestacoes():       
    conexao = conexaobd()
    
    consulta = "SELECT * FROM manifestacoes"
    
    manifestacoes = listarBancoDados(conexao, consulta)
    
    encerrarConexao(conexao)
    
    print(f"\n--------MANIFESTAÇÕES ATIVAS--------")
    
    print(f"Quantidade de Manisfestações Ativas: {len(manifestacoes)}\n")
    
    for i in range(len(manifestacoes)):
        print(f"Código: {manifestacoes[i][0]}\nNome: {manifestacoes[i][1]}\nEmail: {manifestacoes[i][2]}\nTelefone: {manifestacoes[i][3]}\nEndereço: {manifestacoes[i][4]}\nAssunto: {manifestacoes[i][5]}\nDescrição: {manifestacoes[i][6]}\nStatus: {manifestacoes[i][7]}\nSituação: {manifestacoes[i][8]}\nData e Hora: {manifestacoes[i][9]}")
        print("-------------------------------------")
    