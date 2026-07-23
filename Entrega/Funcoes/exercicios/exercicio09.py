def areaRetangulo(base, altura):
    return base * altura


area = areaRetangulo(
    float(input("Digite a base do retângulo: ")),
    float(input("Digite a altura do retângulo: ")),
)
print(f"A área do retângulo é: {area:.2f}m²")
