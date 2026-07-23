# Calculadora IMC
peso = float(input("Digite seu peso em Kg"))
alturacm = float(input("Digite sua altura em centimetros"))
altura = alturacm / 100
imc = peso / (altura**2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    classe = "Abaixo do peso"
elif imc < 25:
    classe = "Peso normal"
elif imc < 30:
    classe = "Sobrepeso"
else:
    classe = "Obesidade"

print(f"Seu IMC é de {imc:.2f}, o que indica que você está na categoria: {classe}")
