aluno = {}


while contagemAluno < 4:
    aluno.append(int(input(f"Digite a matrícula do {contagemAluno + 1}° aluno: ")))
    if matricula[contagemAluno] <= 0:
        print("Matrícula inválida. Por favor, digite um número positivo.")
    else:
        print(matricula)
        contagemAluno += 1
