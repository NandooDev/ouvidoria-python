import bcrypt
import sqlite3

db = sqlite3.connect("manifestacoes.db")

cursor = db.cursor()

def login(email, senha):
        print("Login")
    
    
def cadastro(nome, email, telefone, endereco, senha):
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
                    (nome, email, telefone, endereco, senha)
                    VALUES (?,?,?,?,?)
                    """, (nome, email, telefone, endereco, hashSenha))
            
            db.commit()
            
            return "Registration Successful"