# Classificação de notas
nota = float(input("Digite a nota: "))
if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C ")
else:
    print("Reprovado")
