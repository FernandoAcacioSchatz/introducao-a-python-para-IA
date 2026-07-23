valores = []


def inserirValor(*args):
    while True:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
        if valor == 0 or valor < 0:
            valorTotal = calcularTotalCompra()
            print(f"O valor total da compra é: R${valorTotal:.2f}")
            break
        valores.append(valor)


def calcularTotalCompra():
    return sum(valores)


inserirValor()
