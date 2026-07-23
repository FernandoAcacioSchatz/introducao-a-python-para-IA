produtos = {}

produtos["nome"] = input("Digite o nome do produto: ")
produtos["preço"] = float(input("Digite o preço do produto: "))
produtos["estoque"] = int(input("Digite a quantidade do produto: "))

print(
    "Nome:",
    produtos["nome"],
    ", Preço:",
    produtos["preço"],
    ", Estoque:",
    produtos["estoque"],
)
