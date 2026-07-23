def calcularMedia(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificarAprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def exibirResultado(media, situacao):
    print(f"A média das notas é: {media:.2f}")
    print(f"Situação do aluno: {situacao}")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = calcularMedia(nota1, nota2, nota3)
situacao = verificarAprovacao(media)
exibirResultado(media, situacao)
