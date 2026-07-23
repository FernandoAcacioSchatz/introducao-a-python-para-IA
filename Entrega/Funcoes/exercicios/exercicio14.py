# Cria e preenche a lista em uma única linha
valores = []
desconto = 0


def inserirValor():
    while True:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
        desconto = int(input("Digite o valor do desconto (ou 0 para encerrar): "))
        if valor == 0:
            break
        if desconto == 0:
            break
        desconto = desconto
        valores.append(valor)
        soma = calcularTotalCompra()
        calcularDesconto(soma, desconto)


def calcularTotalCompra():
    return sum(valores)


def calcularDesconto(total, desconto):
    return total - (total * (desconto / 100))


def imprimirCupom(total, desconto):
    inserirValor()
    print("Cupom Fiscal")
    print(f"Total da compra: R${total:.2f}")
    print(f"Desconto aplicado: {desconto}%")
    print(f"Valor final a pagar: R${calcularDesconto(total, desconto):.2f}")


imprimirCupom(calcularTotalCompra(), desconto)
