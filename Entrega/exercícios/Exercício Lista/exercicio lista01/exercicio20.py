produto = []

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ").capitalize()
    if nome.lower() == "sair":
        break
    preco = float(input("Digite o preço do produto: "))
    produto.append({"nome": nome, "preco": preco})
print("\nProdutos cadastrados:")
for p in produto:
    print(f"Produto: {p['nome']}, Preço: R${p['preco']:.2f}")
print()
# soma de todos os preços
soma = sum(p["preco"] for p in produto)
print(f"Soma total dos preços: R${soma:.2f}")
