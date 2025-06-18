from conexaobd import *
from operacoesbd import listarBancoDados, encerrarConexao

def verRespostas():
    conexao = conexaobd()

    consulta = "SELECT * FROM respostas"

    respostas = listarBancoDados(conexao, consulta)

    encerrarConexao(conexao)

    print(f"\n--------Respostas Realizadas--------")
    print(f"Quantidade de Respostas Realizadas: {len(respostas)}\n")

    for i in range(len(respostas)):
        print(f"Código: {respostas[i][0]}\nCódigo da Manifestação: {respostas[i][1]}\nNome do Atendente: {respostas[i][2]}\nEmail do Atendente: {respostas[i][3]}\nResposta: {respostas[i][4]}\nData e Hora: {respostas[i][5]}")
        print("-------------------------------------")