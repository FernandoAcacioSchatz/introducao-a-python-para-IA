valores = []


def inserirValor():
    while True:
        valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
        if valor == 0:
            count = contarPares()
            print(f"Quantidade de valores pares digitados: {count}")
            break
        valores.append(valor)


def contarPares():
    count = 0
    for valor in valores:
        if valor % 2 == 0:
            count += 1
    return count


inserirValor()
