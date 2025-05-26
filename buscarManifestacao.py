import sqlite3

db = sqlite3.connect("manifestacoes.db")

cursor = db.cursor()

escolha = 0

while escolha != 2:
    
    escolha = int(input("1 - Fazer pesquisa por código\n2 - Sair\n"))
    
    if escolha == 1:
        buscarManifestacaoPorCodigo = int(input("\nQual o código da manifestação que você deseja buscar? Ex(1, 2, 3...) "))
        
        cursor.execute("SELECT * FROM manifestacoes WHERE id = ?", (buscarManifestacaoPorCodigo,))
        
        manifestacao = cursor.fetchall()
                
        if manifestacao == []:
            print("Manifestação não existe!\n")
        else:
            print(f"\nCódigo: {manifestacao[0][0]}\nNome: {manifestacao[0][1]}\nEmail: {manifestacao[0][2]}\nTelefone: {manifestacao[0][3]}\nEndereço: {manifestacao[0][4]}\nAssunto: {manifestacao[0][5]}\nDescrição: {manifestacao[0][6]}\nStatus: {manifestacao[0][7]}\nSituação: {manifestacao[0][8]}\nData e Hora: {manifestacao[0][9]}\n")
            
print("Programa finalizado!")