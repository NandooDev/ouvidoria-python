import loginCadastroUser
from excluirManifestacao import *
from manisfestacoes import *
from buscarManifestacao import *
from respostas import *
from conexaobd import *
from operacoesbd import insertNoBancoDados, encerrarConexao

textoAssun = ("Digite o número referente ao assunto que você deseja falar:\n-Elogio: 1\n-Denúncia: 2\n-Dúvida: 3\n")

print("-----------ENTRAR NO SISTEMA DE USUÁRIO-----------")

#LOGIN OU CADASTRO DE USUARIO
while(True):
    loginOrRegister = str(input("Realizar cadastro ou fazer login? (c ou l) "))
    
    loginOrRegister = loginOrRegister.lower()
    
    if (loginOrRegister == "c"):
        
        register = loginCadastroUser.cadastro()
        
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
            
            if tipo == "adm":
                print("Você um ADM, não pode acessar programa de usuário comum!\n")
            else:
                print("Login realizado com sucesso!\n")
                break
        else:
            print("Houve algum erro inesperado ao entrar, por favor tente novamente!\n")
            continue
        
    else:
        print("\nOPÇÃO INVÁLIDA\n")
    
#CRIAR MANIFESTAÇÃO
opcao = 0

while(opcao != 6):
    print("----------OPÇÕES----------")
    opcao = int(input("1 - Criar Manifestação\n2 - Excluir Manifestação\n3 - Ver Manifestações\n4 - Buscar Manifestação\n5 - Ver Respostas\n6 - Sair\n"))
    
    if opcao == 1:
        print("\n-----------CRIAR SOLICITAÇÃO-----------")
        
        assMani = int(input(textoAssun))
        if (assMani != 1 and assMani != 2 and assMani != 3):
            while(True):
                assMani = int(input("Por favor digite uma opção válida:\n"))

                if (assMani == 1 or assMani == 2 or assMani == 3):
                    break
                
        mani = str(input("\nDescreva sua manifestação: "))
        
        conexao = conexaobd()
            
        consulta = """
            INSERT INTO manifestacoes
            (nome, email, telefone, endereco, assuntoManifestacao, descricao, statuss, situacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
        dados = [nome, email, telefone, endereco, assMani, mani, 'Aberta', 'Não respondida']
            
        manifestacao = insertNoBancoDados(conexao, consulta, dados)
            
        encerrarConexao(conexao)
        
        print("\nManifestação criada com sucesso, aguarde sua resposta!\n")
    
    elif opcao == 2:
        excluirManifestacao()
        
    elif opcao == 3:
        verManifestacoes()
        
    elif opcao == 4:
        buscarManifestacao()
        
    elif opcao == 5:
        verRespostas()
    
    elif opcao != 6:
        print("\nOpção Inválida!\n")

print("\nPrograma Finalizado, Volte Sempre!")