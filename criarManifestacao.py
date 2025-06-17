import loginCadastroUser
from excluirManifestacao import *
from conexaobd import *
from operacoesbd import insertNoBancoDados, encerrarConexao

textoAssun = ("Digite o número referente ao assunto que você deseja falar:\n-Elogio: 1\n-Denúncia: 2\n-Dúvida: 3\n")

print("-----------Entrar No Sistema-----------")

#LOGIN OU CADASTRO DE USUARIO
while(True):
    loginOrRegister = str(input("Realizar cadastro ou fazer login? (c ou l) "))
    
    if (loginOrRegister == "c"):
        
        register = loginCadastroUser.cadastro()
        
        if (register == "Email Already Exists"):
            print("Email já existe, tentar novamente!")
            continue
        elif (register == "Telefone Already Exists"):
            print("Telefone já existe, por favor tentar novamente!")
            continue
        elif (len(register) > 0):
            id, nome, email, telefone, endereco, senha, tipo, created = register
            print("Cadastro realizado com sucesso!")
            break
        else:
            print("Houve algum erro inesperado, por favor tentar novamente!")
            continue
    
    elif (loginOrRegister == "l"):                
        login = loginCadastroUser.login()
        
        if (login == "User Not Exists"):
            print("Usuário não existe, por favor realizar cadastro!")
            continue
        elif (login == "Password Invalid"):
            print("Senha inválida, por favor tentar novamente!")
            continue
        elif (len(login) > 0):
            id, nome, email, telefone, endereco, senha, tipo, created = login
            print("Login realizado com sucesso!")
            break
        else:
            print("Houve algum erro inesperado ao entrar, por favor tente novamente!")
            continue
    
#CRIAR MANIFESTAÇÃO
excluirOuCriar = 0

while(excluirOuCriar != 3):
    excluirOuCriar = int(input("1 - Criar Manifestação\n2 - Excluir Manifestação\n3 - Sair\n"))
    
    if excluirOuCriar == 1:
        print("\n-----------Criar Solicitação-----------\n")
        
        assMani = int(input(textoAssun))
        if (assMani != 1 and assMani != 2 and assMani != 3):
            while(True):
                assMani = int(input("Por favor digite uma opção válida:\n"))

                if (assMani == 1 or assMani == 2 or assMani == 3):
                    break
                
        mani = str(input("Descreva sua manifestação:\n"))
        
        conexao = conexaobd()
            
        consulta = """
            INSERT INTO manifestacoes
            (nome, email, telefone, endereco, assuntoManifestacao, descricao, statuss, situacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
        dados = [nome, email, telefone, endereco, assMani, mani, 'Aberta', 'Não respondida']
            
        manifestacao = insertNoBancoDados(conexao, consulta, dados)
            
        encerrarConexao(conexao)
        
        print("Manifestação criada com sucesso, aguarde sua resposta!")
    
    elif excluirOuCriar == 2:
        excluirManifestacao()
    
    else:
        print("Opção Inválida!\n")

print("Programa Finalizado, Volte Sempre!")