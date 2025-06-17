from operacoesbd import criarConexao

def conexaobd():
    return criarConexao("127.0.0.1", "root", "12345", "ouvidoria")