import json

while(True):
    if (str(input("Deseja ver as manifestações? (s ou n) ")) == "s"):
        with open("manifestacoes.json", "r", encoding="latin1") as manifestacoes_json:
            manifestacoes = json.load(manifestacoes_json)
            
        print(f"--------Manifestações Ativas--------")
        print(f"Quantidade de Manisfestações Ativas: {len(manifestacoes)}")
        
        print(manifestacoes)

        for i in range(len(manifestacoes)):
            print(f"Nome: {manifestacoes[i]['Nome']}\nEmail: {manifestacoes[i]['Email']}\nTelefone: {manifestacoes[i]['Telefone']}\nEndereço: {manifestacoes[i]['Endereço']}\nAssunto: {manifestacoes[i]['Assunto']}\nDescrição: {manifestacoes[i]['Descrição']}\nStatus: {manifestacoes[i]['Status']}\nSituação: {manifestacoes[i]['Situação']}")
            print("-------------------------------------")
    else:
        break