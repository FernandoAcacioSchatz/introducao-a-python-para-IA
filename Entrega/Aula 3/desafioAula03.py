vendas = [
    850,
    1200,
    980,
    1560,
    720,
    1100,
    890,
    1340,
    630,
    1450,
    970,
    1280,
    810,
    1620,
    750,
    1050,
    920,
    1380,
    660,
    1490,
]

while True:
    entrada = input("\nDigite uma nova meta para análise: R$ ")
    nova_meta = float(entrada)
    if nova_meta > 0:
        meta = nova_meta
        print(f"\nNova meta definida: R$ {meta}")
    else:
        print("Valor invalido. Digite um valor valido.")
        continue

    # Resetar a cada nova meta
    soma = 0
    contagem = 0
    dias_acima_meta = []
    primeiroDiaAcima1500 = 0

    for i, valor in enumerate(vendas):
        soma += valor
        contagem += 1

        if valor > meta:
            dias_acima_meta.append(valor)

        if valor > 1500 and primeiroDiaAcima1500 == 0:
            primeiroDiaAcima1500 = valor
            print(f"Primeira venda acima de R$1500: {i + 1}° dia → R${valor}")

    media = soma / contagem
    maior = max(vendas)

    print(f"\nMaior venda: R${maior:.2f} no {vendas.index(maior) + 1}° dia")
    print(f"Total de vendas: R${soma:.2f}")
    print(f"Média de vendas: R${media:.2f}")
    print(f"Dias acima de R${meta:.2f}: {len(dias_acima_meta)}")
