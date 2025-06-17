import bcrypt
from conexaobd import *
from operacoesbd import listarBancoDados, insertNoBancoDados, encerrarConexao

def login():
    conexao = conexaobd()
    
    #DADOS
    email = str(input("Qual seu email?\n"))
    if (email.count("@") == 0 or email.count("@") > 1):
        while(True):
            email = str(input("Por favor digite um email válido:\n"))

            if (email.count("@") == 1):
                break
                
    senha = str(input("Digite sua senha de acesso:\n"))
    
    #VERIFICACOES
    consulta = "SELECT senha FROM users WHERE email = %s"
    
    emailAlreadyExists = listarBancoDados(conexao, consulta, [email])
    
    if (len(emailAlreadyExists) == 0):
        return "User Not Exists"
    else:
        senhaValida = bcrypt.checkpw(senha.encode(), emailAlreadyExists[0][0].encode())
        
        if (senhaValida):
            consulta = "SELECT * FROM users WHERE email = %s"
            
            user = listarBancoDados(conexao, consulta, [email])
            
            encerrarConexao(conexao)
            
            return (user[0])
        else:
            encerrarConexao(conexao)
            
            return "Password Invalid"
    
    
def cadastro(tipo="user"):
    conexao = conexaobd()
    
    #DADOS
    nome = str(input("Qual o seu nome?\n"))
        
    email = str(input("Qual seu email?\n"))
    if (email.count("@") == 0 or email.count("@") > 1):
        while(True):
            email = str(input("Por favor digite um email válido:\n"))

            if (email.count("@") == 1):
                    break
                    
    telefone = str(input("Qual seu telefone?\n"))
            
    endereco = str(input("Qual seu endereço?\n"))
            
    senha = str(input("Digite sua senha de acesso:\n"))
    
    #VERIFICACOES
    
    consulta = "SELECT senha FROM users WHERE email = %s"
    
    emailAlreadyExists = listarBancoDados(conexao, consulta, [email])
    
    if (len(emailAlreadyExists) > 0):
        return "Email Already Exists"
    else:
        consulta = "SELECT * FROM users WHERE telefone = %s"
        
        telefoneAlreadyExists = listarBancoDados(conexao, consulta, [telefone])
        
        if (len(telefoneAlreadyExists) > 0):
            return "Telefone Already Exists"
        else:
            hashSenha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            
            consulta = """
                    INSERT INTO users
                    (nome, email, telefone, endereco, senha, tipo)
                    VALUES (%s,%s,%s,%s,%s,%s)
                    """        
                    
            dados = [nome, email, telefone, endereco, hashSenha, tipo]
                
            insertNoBancoDados(conexao, consulta, dados)  
            
            consulta = "SELECT * FROM users WHERE email = %s"
            
            user = listarBancoDados(conexao, consulta, [email])
                        
            encerrarConexao(conexao)
            
            return (user[0])