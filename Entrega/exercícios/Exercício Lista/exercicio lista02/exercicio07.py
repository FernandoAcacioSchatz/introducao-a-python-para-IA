num = []

for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    num.append(numero)

print(*num, sep=", ", end=".\n")

for num in num:
    if num % 2 == 0:
        print(num, "é par.")
    else:
        print(num, "é ímpar.")
