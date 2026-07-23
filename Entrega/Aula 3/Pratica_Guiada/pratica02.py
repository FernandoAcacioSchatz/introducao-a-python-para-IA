soma = 0
for i in range(1, 51):
    soma += i
print(f"\nA soma dos números de 1 a 50 é {soma}")

cont = 0
for i in range(1, 51):
    if i % 3 == 0:
        cont += 1
print(f"Existem {cont} números múltiplos de 3 entre 1 e 50")
