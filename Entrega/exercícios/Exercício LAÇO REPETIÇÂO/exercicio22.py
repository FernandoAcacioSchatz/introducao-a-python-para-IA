parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
desconto = 0.20
valorTotalCarro = 0
valorParcela = 0
valorCarro = float(input("Digite o valor do carro: "))

print(f"{'Parcelas':<12} {'Acréscimo':>10}")
print("-" * 24)

for p in parcelas:
    acrescimo = (parcelas.index(p) + 1) * 3
    print(f"{p:<12} {acrescimo:>9}%")
print("-" * 24)
print()

parcela = int(input("Digite o número de parcelas desejado: "))
if parcela in parcelas:
    acrescimo = (parcela / 2) / 100
    valorTotalCarro = valorCarro + (valorCarro * acrescimo)
    valorParcela = valorTotalCarro / parcela
    print(f"{acrescimo * 100:.0f}%")
    print(f"{valorParcela:.2f}")
    print(f"{valorTotalCarro:.2f}")
elif parcela == 0:
    valorTotalCarro = valorCarro - (valorCarro * desconto)
    print(f"{valorTotalCarro:.2f}")
else:
    print("parcela indisponivel")
