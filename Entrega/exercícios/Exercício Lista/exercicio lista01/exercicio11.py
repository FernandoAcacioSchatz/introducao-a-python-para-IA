numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(8)]
numerosPositivos = [numero for numero in numeros if numero >= 0]

print(f"Lista de números: {', '.join(map(str, numeros))}")
print(f"Lista de números positivos: {', '.join(map(str, numerosPositivos))}")
