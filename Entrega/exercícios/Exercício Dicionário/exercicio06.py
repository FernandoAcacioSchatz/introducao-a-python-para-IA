agendas = {}

while True:
    nome = input("Digite o nome, listar ou sair para encerrar: ")
    if nome == "sair":
        break
    elif nome == "listar":

        if not agendas:
            print("A agenda está vazia.")
        else:

            for contato, telefone in agendas.items():
                print(f"Nome: {contato} - Telefone: {telefone}")
    else:
        telefone = input("Digite o telefone: ")
        agendas[nome] = telefone
