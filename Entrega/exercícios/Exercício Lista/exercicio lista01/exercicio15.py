nomes = []

while True:
    nome = input("Digite o nome ou fim para sair: ").lower()
    if nome == "fim":
        break
    else:
        nomes.append(nome)

print(f"{', '.join(nomes.capitalize() for nomes in nomes)}")
