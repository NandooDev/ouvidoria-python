import loginCadastroUser
import sqlite3

db = sqlite3.connect("manifestacoes.db")

cursor = db.cursor()

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
        
while(True):
    
    while(True):
        codigo_manifestacao = int(input("Qual o código da manifestação que você deseja responder? "))

        cursor.execute("SELECT * FROM manifestacoes WHERE id = ?", (codigo_manifestacao,))
        
        manifestacaoExist = len(cursor.fetchall())
        if (manifestacaoExist > 0):
            break
        else:
            print("Essa manifestação não existe, digite uma manifestação válida!")
            continue

    resposta = str(input("Qual sua resposta para essa manifestação?\n"))
    
    cursor.execute("""
            INSERT INTO respostas
            (codigo_manifestacao, nome_atendente, email_atendente, resposta)
            VALUES (?,?,?,?)
            """, (codigo_manifestacao, nome, email, resposta))
    
    cursor.execute("""
            UPDATE manifestacoes
            SET statuss = "Fechada", situacao = "Respondida"
            WHERE id = ?
            """, (codigo_manifestacao,))
    
    db.commit()
    
    print("Resposta realizada!")