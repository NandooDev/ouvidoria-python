import json
manifestacoes = []
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
    
    nova_mani = {"Nome": nome,
                 "Email": email,
                 "Telefone": telefone,
                 "Endereço": endereco,
                 "Assunto": assMani,
                 "Descrição": mani,
                 "Status": "Aberta",
                 "Situação": "Não respondida"}

    manifestacoes.append(nova_mani)

    with open("manifestacoes.json", "w", encoding="utf-8") as manifestacoes_json:
        json.dump(manifestacoes, manifestacoes_json, ensure_ascii=False, indent=4)