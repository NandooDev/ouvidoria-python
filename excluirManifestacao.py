from conexaobd import *
from operacoesbd import excluirBancoDados, encerrarConexao

def excluirManifestacao(): 
    buscarManifestacaoPorCodigo = int(input("\nQual o código da manifestação que você deseja excluir? Ex(1, 2, 3...) "))

    conexao = conexaobd()
            
    consulta = "DELETE FROM manifestacoes WHERE id = %s"
            
    linhasAfetadas = excluirBancoDados(conexao, consulta, [buscarManifestacaoPorCodigo])

    if linhasAfetadas > 0:
        print("Manifestação excluída com sucesso!\n")
    elif linhasAfetadas == 0:
        print("Manifestação não encontrada!\n")
    else:
        print("Manifestação não encontrada!\n")
                
    encerrarConexao(conexao)
