textoAssun = ("Digite o número referente ao assunto que você deseja falar:\n-Elogio: 1\n-Denúncia: 2\n-Dúvida: 3\n")
manifestações = []

while(True):
    nome = str(input("Qual o seu nome?\n"))
    email = str(input("Qual seu email?\n"))
    if (email.count("@") == 0 or email.count("@") > 1):
        while(True):
            email = str(input("Por favor digite um email válido:\n"))

            if (email.count("@") == 1):
                break
    telefone = str(input("Qual seu telefone?\n"))
    assMani = int(input(textoAssun))
    if (assMani != 1 and assMani != 2 and assMani != 3):
        while(True):
            assMani = int(input("Por favor digite uma opção válida:\n"))

            if (assMani == 1 or assMani == 2 or assMani == 3):
                break
    mani = str(input("Descreva sua manifestação:\n"))

    manifestações.append([nome, email, telefone, assMani, mani])

    print(f"--------Manifestações Ativas--------")
    for i in manifestações:
        print(f"Quantidade de Manisfestações Ativas: {len(manifestações)}")
        print(f"Nome: {i[0]}\nEmail: {i[1]}\nTelefone: {i[2]}\nAssunto: {i[3]}\nDescrição: {i[4]}")
        print("-------------------------------------")