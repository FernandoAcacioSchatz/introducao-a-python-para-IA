numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(numero)
print()


pares = [numero for numero in numeros if numero % 2 == 0]


print(*numeros, sep=", ", end=".\n")
print(*pares, sep=", ", end=".\n")
