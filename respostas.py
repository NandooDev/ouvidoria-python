from conexaobd import *
from operacoesbd import listarBancoDados, encerrarConexao

while(True):
    if (str(input("Deseja ver as respostas realizadas? (s ou n) ")) == "s"):
        conexao = conexaobd()
        
        consulta = "SELECT * FROM manifestacoes"
        
        respostas = listarBancoDados(conexao, consulta)
        
        encerrarConexao(conexao)
        
        print(f"--------Respostas Realizadas--------")
        print(f"Quantidade de Respostas Realizadas: {len(respostas)}")

        for i in range(len(respostas)):
            print(f"Código: {respostas[i][0]}\nCódigo da Manifestação: {respostas[i][1]}\nNome do Atendente: {respostas[i][2]}\nEmail do Atendente: {respostas[i][3]}\nResposta: {respostas[i][4]}\nData e Hora: {respostas[i][5]}")
            print("-------------------------------------")
    else:
        break