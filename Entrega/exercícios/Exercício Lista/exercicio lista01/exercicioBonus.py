from statistics import mean

precos = []

for i in range(10):
    preco = float(input(f"Digite o preço o {i + 1 }° produto : "))
    while preco <= 0:
        print("Preço inválido. Digite um valor positivo.")
        preco = float(input("Digite o preço do produto: "))
    precos.append(preco)

soma = sum(1 for preco in precos if preco > 100)

print(max(precos))
print(min(precos))
print(f"A média dos preços dos produtos é: {mean(precos)}")
print(soma)
