turma = [
    {"nome": "Ana", "nota": 8.5, "turma": "A"},
    {"nome": "Bruno", "nota": 4.0, "turma": "A"},
    {"nome": "Carla", "nota": 9.0, "turma": "B"},
    {"nome": "Diego", "nota": 6.5, "turma": "B"},
]

soma = 0

for aluno in turma:
    status = "Aprovado" if aluno["nota"] >= 7 else "Reprovado"
    print(f"{aluno['nome']} - Nota: {aluno['nota']} - {status}")
