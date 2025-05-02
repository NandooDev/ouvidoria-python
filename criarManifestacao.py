import sqlite3

db = sqlite3.connect('manifestacoes.db')

textoAssun = ("Digite o número referente ao assunto que você deseja falar:\n-Elogio: 1\n-Denúncia: 2\n-Dúvida: 3\n")

while(True):
    print("-----------Criar Solicitação-----------")
    
    nome = str(input("Qual o seu nome?\n"))
    
    email = str(input("Qual seu email?\n"))
    if (email.count("@") == 0 or email.count("@") > 1):
        while(True):
            email = str(input("Por favor digite um email válido:\n"))

            if (email.count("@") == 1):
                break
            
    telefone = str(input("Qual seu telefone?\n"))
    
    endereco = str(input("Qual seu endereço?\n"))
    
    assMani = int(input(textoAssun))
    if (assMani != 1 and assMani != 2 and assMani != 3):
        while(True):
            assMani = int(input("Por favor digite uma opção válida:\n"))

            if (assMani == 1 or assMani == 2 or assMani == 3):
                break
            
    mani = str(input("Descreva sua manifestação:\n"))
    
    db.execute("""
        INSERT INTO manifestacoes
        (nome, email, telefone, endereco, assuntoManifestacao, descricao, statuss, situacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, telefone, endereco, assMani, mani, 'Aberta', 'nao resp'))

    db.commit()
    
    print("Manifestação criada com sucesso, aguarde sua resposta!")