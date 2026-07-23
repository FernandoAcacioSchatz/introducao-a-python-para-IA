def calcularMedia(n1, n2, n3):
    return (n1 + n2 + n3) / 3


resultado = calcularMedia(
    float(input("Digite a primeira nota: ")),
    float(input("Digite a segunda nota: ")),
    float(input("Digite a terceira nota: ")),
)
print(f"A média das notas é: {resultado:.2f}")
