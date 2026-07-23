num = set()
for i in range(5):
    numero = float(input("Digite um número: "))
    num.add(numero)

print("Números digitados:", *map(str, num), sep=", ", end=".\n")
