cliente = input("Digite o nome do cliente: ")
valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))
desconto = 0.00


def cadastrarCliente(nome):
    return nome


def receberValores(valor1, valor2):
    return valor1, valor2


def calcularMedia(valor1, valor2):
    return (valor1 + valor2) / 2


def somaValores(valor1, valor2):
    return valor1 + valor2


def verificarDesconto(soma):
    if soma > 150:
        return 0.10
    else:
        return 0.00


def exibirCupom(nome, valor1, valor2):

    media = calcularMedia(valor1, valor2)
    soma = somaValores(valor1, valor2)
    desconto = verificarDesconto(soma)
    print("Cupom Fiscal")
    print(f"Cliente: {nome}")
    print(f"Valor 1: {valor1}")
    print(f"Valor 2: {valor2}")
    print(f"Média da compra: {media:.2f}")
    print(f"Soma da compra: {soma}")
    print(f"Desconto aplicado: {desconto * 100}%")
    print(f"Valor final a pagar: {soma - (soma * desconto)}")


exibirCupom(cadastrarCliente(cliente), *receberValores(valor1, valor2))
