pesos = []
idades = []
pesoFaixa1a10 = []
pesoFaixa11a20 = []
pesoFaixa21a30 = []
pesoFaixa31Mais = []
qnt = 3

for i in range(qnt):
    pesos.append(float(input(f"Digite o peso da pessoa {i + 1}: ")))
    if pesos[i] < 0:
        print("Peso inválido")
        break
    idades.append(int(input(f"Digite a idade da pessoa {i + 1}: ")))
    if idades[i] > 115 or idades[i] < 0:
        print("Idade inválida")
        break
    elif 1 <= idades[i] <= 10:
        pesoFaixa1a10.append(pesos[i])
    elif 11 <= idades[i] <= 20:
        pesoFaixa11a20.append(pesos[i])
    elif 21 <= idades[i] <= 30:
        pesoFaixa21a30.append(pesos[i])
    elif idades[i] >= 31:
        pesoFaixa31Mais.append(pesos[i])
if len(pesos) == qnt:
    if len(pesoFaixa1a10) > 0:
        mediaFaixa1a10 = sum(pesoFaixa1a10) / len(pesoFaixa1a10)
        print(f"Média de peso para a faixa etária de 1 a 10 anos: {mediaFaixa1a10:.2f}")

    else:
        mediaFaixa1a10 = 0
        print(
            "Não há pessoas na faixa etária de 1 a 10 anos para calcular a média de peso."
        )
    if len(pesoFaixa11a20) > 0:
        mediaFaixa11a20 = sum(pesoFaixa11a20) / len(pesoFaixa11a20)
        print(
            f"Média de peso para a faixa etária de 11 a 20 anos: {mediaFaixa11a20:.2f}"
        )

    else:
        mediaFaixa11a20 = 0
        print(
            "Não há pessoas na faixa etária de 11 a 20 anos para calcular a média de peso."
        )
    if len(pesoFaixa21a30) > 0:
        mediaFaixa21a30 = sum(pesoFaixa21a30) / len(pesoFaixa21a30)
        print(
            f"Média de peso para a faixa etária de 21 a 30 anos: {mediaFaixa21a30:.2f}"
        )
    else:
        mediaFaixa21a30 = 0
        print(
            "Não há pessoas na faixa etária de 21 a 30 anos para calcular a média de peso."
        )
    if len(pesoFaixa31Mais) > 0:
        mediaFaixa31Mais = sum(pesoFaixa31Mais) / len(pesoFaixa31Mais)
        print(
            f"Média de peso para a faixa etária de 31 anos ou mais: {mediaFaixa31Mais:.2f}"
        )
    else:
        mediaFaixa31Mais = 0
        print(
            "Não há pessoas na faixa etária de 31 anos ou mais para calcular a média de peso."
        )
else:
    print("Não foi possível calcular as médias devido a dados inválidos.")
