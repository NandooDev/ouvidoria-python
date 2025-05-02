import bcrypt
import sqlite3

db = sqlite3.connect("manifestacoes.db")

cursor = db.cursor()

def login():
    #DADOS
    email = str(input("Qual seu email?\n"))
    if (email.count("@") == 0 or email.count("@") > 1):
        while(True):
            email = str(input("Por favor digite um email válido:\n"))

            if (email.count("@") == 1):
                break
                
    senha = str(input("Digite sua senha de acesso:\n"))
    
    #VERIFICACOES
    
    cursor.execute("SELECT senha FROM users WHERE email = ?", (email,))
    
    user = cursor.fetchall()
    
    if (len(user) == 0):
        return "User Not Exists"
    else:
        senhaValida = bcrypt.checkpw(senha.encode(), user[0][0])
        
        if (senhaValida):
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            
            dados = cursor.fetchall()
            
            return (dados[0])
        else:
            return "Password Invalid"
    
def cadastro(tipo="user"):
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
    
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    
    emailAlreadyExists = cursor.fetchall()
    
    if (len(emailAlreadyExists) > 0):
        return "Email Already Exists"
    else:
        cursor.execute("SELECT * FROM users WHERE telefone = ?", (telefone,))
        
        telefoneAlreadyExists = cursor.fetchall()
        
        if (len(telefoneAlreadyExists) > 0):
            return "Telefone Already Exists"
        else:
            hashSenha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            
            cursor.execute("""
                    INSERT INTO users
                    (nome, email, telefone, endereco, senha, tipo)
                    VALUES (?,?,?,?,?,?)
                    """, (nome, email, telefone, endereco, hashSenha, tipo))            
            
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            
            dados = cursor.fetchall()
            
            db.commit()
            
            return (dados[0])