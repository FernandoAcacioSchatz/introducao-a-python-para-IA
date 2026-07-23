notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")
