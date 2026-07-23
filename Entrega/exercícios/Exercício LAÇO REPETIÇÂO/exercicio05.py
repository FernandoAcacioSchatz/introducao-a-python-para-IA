print("Digite três valores")
a = float(input("Valor A: "))
b = float(input("Valor B: "))
c = float(input("Valor C: "))
print()
if a == b == c:
    print(f"Os três valores são iguais. A = {a}, B = {b}, C = {c}")
else:
    valores = [a, b, c]
    print(*valores)
    valores.sort()
    for i in range(len(valores)):
        if i == len(valores) - 1:
            print(f"{valores[i]}", end="\n")
            valores.reverse()
            print(*valores)
        else:
            print(f"{valores[i]} ", end="")
    print()
