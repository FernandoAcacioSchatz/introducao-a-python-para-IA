notas = [7.5, 8.0, 6.5, 9.0, 5.5]
soma = 0
for i, nota in enumerate(notas):
    print(f"Aluno {i+1}: {nota:.1f}")
    soma += nota
media = soma / len(notas)
print(f"Média: {media:.1f}")
