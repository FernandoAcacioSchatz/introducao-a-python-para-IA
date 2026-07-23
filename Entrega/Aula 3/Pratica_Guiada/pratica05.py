valores = [12, 7, 35, 5, 28, 3, 19]
for i, v in enumerate(valores):
    if v > 20:
        print(f"Primeiro número maior que 20 é {v} na posição {i}")
        break

print("Menores que 10: ")
for v in valores:
    if v >= 10:
        continue
    print(v)
