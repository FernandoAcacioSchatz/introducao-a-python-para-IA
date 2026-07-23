produto = {
    "nome": "Notebook",
    "preco": 2500.00,
    "estoque": 10,
    "categoria": "eletrônicos",
}

produto["desconto"] = 0.1

precoFinal = produto["preco"] * (1 - produto["desconto"])
print(produto.get("garantia", "sem garantia"))
print(produto.get("tema"))

print(f"Produto: {produto['nome']}")
print(f"Estoque do produto: {produto['estoque']}")
print(f"Categoria do produto: {produto['categoria']}")
