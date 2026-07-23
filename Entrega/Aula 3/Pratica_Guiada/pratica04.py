numero = 0
while numero < 1 or numero > 10:
    numero = int(input("Digite um número entre 1 e 10: "))
    if numero < 1 or numero > 10:
        print("Numero inválido. Tente novamente.")
print(f"{numero} ao quadrado é {numero **2}")
