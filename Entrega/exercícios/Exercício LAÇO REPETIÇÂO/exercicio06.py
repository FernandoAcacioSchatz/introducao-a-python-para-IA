lojaB = 54000
lojaA = 0
valores = []
diferenca = 0

for i in range(5):
    valor = float(input(f"Digite o valor do produto {i+1}: "))
    valores.append(valor)
    lojaA = sum(valores)
print()
if lojaA > lojaB:
    print(f"O faturamento da loja A = R${lojaA:.2f}")
    print(f"O faturamento da loja B = R${lojaB:.2f}")
    diferenca = lojaA - lojaB
    print(f"A loja A teve um faturamento maior que a loja B em R${diferenca:.2f}")
elif lojaB > lojaA:
    print(f"O faturamento da loja A = R${lojaA:.2f}")
    print(f"O faturamento da loja B = R${lojaB:.2f}")
    diferenca = lojaB - lojaA
    print(f"A loja B teve um faturamento maior que a loja A em R${diferenca:.2f}")
else:
    print(f"O faturamento da loja A = {lojaA:.2f}")
    print(f"O faturamento da loja B = {lojaB:.2f}")
    print("As lojas A e B tiveram o mesmo faturamento.")
