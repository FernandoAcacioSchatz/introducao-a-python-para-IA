estoque = {
    "notebook": 10,
    "mouse": 100,
    "teclado": 50,
    "cadeira gamer": 20,
    "monitor": 30,
}
estoqueBaixo = {}
total = 0
for produto, qnt in estoque.items():
    total += qnt
    if qnt < 25:
        estoqueBaixo[produto] = qnt

for produto, qnt in estoqueBaixo.items():
    print(f"O produto {produto} tem apenas {qnt} unidades em estoque")
print(f"O total de produtos em estoque é de {total} unidades")
