contadorMais50 = 0
contadorAlturaEntreDezeVinte = 0
contadorPeso40 = 0
somaAltura = 0
lista = 5


for i in range(lista):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa (em metros) {i+1}: "))
    peso = float(input(f"Digite o peso da pessoa (em kg) {i+1}: "))
    print()

    if idade >= 50:
        contadorMais50 += 1

    if idade >= 10 and idade <= 20:
        contadorAlturaEntreDezeVinte += 1
        somaAltura += altura

    if peso < 40:
        contadorPeso40 += 1

if contadorAlturaEntreDezeVinte > 0:
    mediaAltura = somaAltura / contadorAlturaEntreDezeVinte
    print(
        f"A média da altura das pessoas com idade entre 10 e 20 anos é de {mediaAltura:.2f}"
    )
else:
    print("Não tem pessoas com idade entre 10 e 20 anos")
porcentagem = (contadorPeso40 / lista) * 100
print(f"{contadorMais50:.0f} pessoas tem mais de 50 anos")

print(f"A porcentagem das pessoas com peso inferior a 40 quilos é de {porcentagem}%")
