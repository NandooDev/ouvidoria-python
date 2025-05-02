import sqlite3

db = sqlite3.connect('manifestacoes.db')

cursor = db.cursor()

while(True):
    if (str(input("Deseja ver as manifestações? (s ou n) ")) == "s"):
        cursor.execute("SELECT * FROM manifestacoes")
        
        manifestacoes = cursor.fetchall()
        
        db.commit()    
        
        print(f"--------Manifestações Ativas--------")
        print(f"Quantidade de Manisfestações Ativas: {len(manifestacoes)}")

        for i in range(len(manifestacoes)):
            print(f"Código: {manifestacoes[i][0]}\nNome: {manifestacoes[i][1]}\nEmail: {manifestacoes[i][2]}\nTelefone: {manifestacoes[i][3]}\nEndereço: {manifestacoes[i][4]}\nAssunto: {manifestacoes[i][5]}\nDescrição: {manifestacoes[i][6]}\nStatus: {manifestacoes[i][7]}\nSituação: {manifestacoes[i][8]}")
            print("-------------------------------------")
    else:
        break