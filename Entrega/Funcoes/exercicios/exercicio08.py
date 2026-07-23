def calcularTabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


numero = int(input("Digite um número para calcular a tabuada: "))
calcularTabuada(numero)
