import loginCadastroUser
from manisfestacoes import *
from respostas import *
from conexaobd import *
from operacoesbd import insertNoBancoDados, listarBancoDados, atualizarBancoDados, encerrarConexao

print("-----------ENTRAR NO SISTEMA-----------")

while(True):
    loginOrRegister = str(input("Realizar cadastro ou fazer login? (c ou l) "))
    
    loginOrRegister = loginOrRegister.lower()
    
    if (loginOrRegister == "c"):
        
        register = loginCadastroUser.cadastro("adm")
        
        if (register == "Email Already Exists"):
            print("Email já existe, tentar novamente!\n")
            continue
        elif (register == "Telefone Already Exists"):
            print("Telefone já existe, por favor tentar novamente!\n")
            continue
        elif (len(register) > 0):
            id, nome, email, telefone, endereco, senha, tipo, created = register
            print("Cadastro realizado com sucesso!\n")
            break
        else:
            print("Houve algum erro inesperado, por favor tentar novamente!\n")
            continue
    
    elif (loginOrRegister == "l"):                
        login = loginCadastroUser.login()
        
        if (login == "User Not Exists"):
            print("Usuário não existe, por favor realizar cadastro!\n")
            continue
        elif (login == "Password Invalid"):
            print("Senha inválida, por favor tentar novamente!\n")
            continue
        elif (len(login) > 0):
            id, nome, email, telefone, endereco, senha, tipo, created = login

            if tipo != "adm":
                print("ACESSO NEGADO, VOCÊ NÃO É UM ADM\n")
                continue
            else:
                print("Login realizado com sucesso!\n")
                break
        else:
            print("Houve algum erro inesperado ao entrar, por favor tente novamente!\n")
            continue
        
    else:
        print("\nOPÇÃO INVÁLIDA\n")
        
opcao = 0

while(opcao != 4):
    print("----------OPÇÕES----------")
    opcao = int(input("1 - Realizar Respostas\n2 - Ver Manifestações\n3 - Ver Respostas\n4 - Sair\n"))
        
    if opcao == 1:
        conexao = conexaobd()
    
        while(True):
            codigo_manifestacao = int(input("\nQual o código da manifestação que você deseja responder? "))

            consulta = "SELECT * FROM manifestacoes WHERE id = %s"
            
            manifestacaoExist = listarBancoDados(conexao, consulta, [codigo_manifestacao])
            
            if (len(manifestacaoExist) > 0):
                break
            else:
                print("Essa manifestação não existe, digite uma manifestação válida!")
                continue

        resposta = str(input("\nQual sua resposta para essa manifestação? "))
        
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
        
        print("Resposta Realizada Com Sucesso!\n")
        
    elif opcao == 2:
        verManifestacoes()
    
    elif opcao == 3:
        verRespostas()
        
    elif opcao != 5:
        print("\nOpção Inválida\n")
        
print("\nPrograma Finalizado Com Sucesso!")