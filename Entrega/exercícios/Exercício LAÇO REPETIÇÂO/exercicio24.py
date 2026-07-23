primos = []
numeros = []

while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        break
    else:
        numeros.append(numero)
        if (len(numeros)) > 0:
            for i in range(1, numero):
                if numero % i == 0:
                    break
            else:
                primos.append(numero)

if primos.__len__() == 0:
    print("Não foram digitados números primos.")
else:
    print(*primos)
print(*numeros)
