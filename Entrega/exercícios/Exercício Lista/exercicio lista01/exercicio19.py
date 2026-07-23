matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento linha {i+1} coluna {j+1}: "))
        linha.append(valor)

        print("\nMatriz atual:")
        for l in range(len(matriz)):
            print(" ".join(map(str, matriz[l])))
        print(" ".join(map(str, linha)))
        print()

    matriz.append(linha)


print("\nMatriz:")
for linha in matriz:
    print(" ".join(map(str, linha)))

soma = sum(matriz[i][i] for i in range(3))

print(f"\nSoma da diagonal principal: {soma}")
