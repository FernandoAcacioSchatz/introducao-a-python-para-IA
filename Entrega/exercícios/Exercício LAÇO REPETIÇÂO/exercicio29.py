contagemAluno = 0
mediaNotas = []
faltas = []  # ← lista para guardar as faltas de cada aluno
presenca = 45

while contagemAluno < 3:
    falta = int(input(f"Digite a quantidade de faltas do {contagemAluno + 1}° aluno: "))
    if falta <= 0 or falta > presenca:
        print(
            f"Quantidade de faltas inválida. Por favor, digite um número entre 1 e {presenca}."
        )
    else:
        nota = []
        contagem = 0
        while contagem < 3:
            notas = float(input(f"Digite a {contagem + 1}° nota do aluno: "))
            if notas < 0 or notas > 10:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
            else:
                nota.append(notas)
                contagem += 1

        mediaNotas.append(sum(nota) / len(nota))  # ← após coletar as 3 notas
        faltas.append(falta)  # ← guarda a falta do aluno
        contagemAluno += 1

for i, media in enumerate(mediaNotas):
    print(f"\nMédia do aluno {i + 1}: {media:.2f}")
    if media >= 6 and presenca - faltas[i] >= 40:
        print(f"Aluno {i + 1}: Aprovado")
    elif media >= 6 and presenca - faltas[i] < 40:
        print(
            f"Aluno {i + 1}: Reprovado por não ter atingido o número mínimo de presença"
        )
    else:
        print(f"Aluno {i + 1}: Reprovado")
