import loginCadastroUser
from conexaobd import *
from operacoesbd import insertNoBancoDados, listarBancoDados, atualizarBancoDados, encerrarConexao

while(True):
    loginOrRegister = str(input("Realizar cadastro ou fazer login? (c ou l) "))
    
    if (loginOrRegister == "c"):
        
        register = loginCadastroUser.cadastro("adm")
        
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
        
respostaOuSair = 0

while(respostaOuSair != 2):
    
    respostaOuSair = int(input("1 - Realizar Respostas\n2 - Sair\n"))
        
    if respostaOuSair == 1:
        conexao = conexaobd()
    
        while(True):
            codigo_manifestacao = int(input("Qual o código da manifestação que você deseja responder? \n"))

            consulta = "SELECT * FROM manifestacoes WHERE id = %s"
            
            manifestacaoExist = listarBancoDados(conexao, consulta, [codigo_manifestacao])
            
            if (len(manifestacaoExist) > 0):
                break
            else:
                print("Essa manifestação não existe, digite uma manifestação válida!\n")
                continue

        resposta = str(input("Qual sua resposta para essa manifestação?\n"))
        
        consulta = """
                INSERT INTO respostas
                (codigo_manifestacao, nome_atendente, email_atendente, resposta)
                VALUES (%s,%s,%s,%s)
                """
        
        dados = [codigo_manifestacao, nome, email, resposta]
        
        insertNoBancoDados(conexao, consulta, dados)
        
        consulta = """
                UPDATE manifestacoes
                SET statuss = "Fechada", situacao = "Respondida"
                WHERE id = %s
                """
        
        atualizarBancoDados(conexao, consulta, [codigo_manifestacao])
        
        encerrarConexao(conexao)
        
        print("Resposta Realizada Com Sucesso!")

print("Programa Finalizado Com Sucesso!")