from conexaobd import *
from operacoesbd import listarBancoDados, encerrarConexao

escolha = 0

while escolha != 2:
    
    escolha = int(input("1 - Fazer pesquisa por código\n2 - Sair\n"))
    
    if escolha == 1:
        buscarManifestacaoPorCodigo = int(input("\nQual o código da manifestação que você deseja buscar? Ex(1, 2, 3...) "))

        conexao = conexaobd()
        
        consulta = "SELECT * FROM manifestacoes WHERE id = %s"
        
        manifestacao = listarBancoDados(conexao, consulta, [buscarManifestacaoPorCodigo])
        
        encerrarConexao(conexao)
                
        if manifestacao == []:
            print("Manifestação não existe!\n")
        else:
            print(f"\nCódigo: {manifestacao[0][0]}\nNome: {manifestacao[0][1]}\nEmail: {manifestacao[0][2]}\nTelefone: {manifestacao[0][3]}\nEndereço: {manifestacao[0][4]}\nAssunto: {manifestacao[0][5]}\nDescrição: {manifestacao[0][6]}\nStatus: {manifestacao[0][7]}\nSituação: {manifestacao[0][8]}\nData e Hora: {manifestacao[0][9]}\n")
            
print("Programa finalizado!")