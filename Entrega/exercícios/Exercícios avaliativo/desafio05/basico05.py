nota = float(input("Informe a nota do aluno: "))

if nota < 0 or nota > 10:
    print("Nota inválida!")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
