import sqlite3

db = sqlite3.connect("manifestacoes.db")

cursor = db.cursor()

escolha = 0

while escolha != 2:
    escolha = int(input("1 - Excluir manifestação por código\n2 - Sair\n"))
    
    if escolha == 1:
        buscarManifestacaoPorCodigo = int(input("\nQual o código da manifestação que você deseja excluir? Ex(1, 2, 3...) "))

        cursor.execute("DELETE FROM manifestacoes WHERE id = ?", (buscarManifestacaoPorCodigo,))
        db.commit()  

        if cursor.rowcount > 0:
            print("Manifestação excluída com sucesso!")
        else:
            print("Manifestação não encontrada!")

print("Programa finalizado!")
