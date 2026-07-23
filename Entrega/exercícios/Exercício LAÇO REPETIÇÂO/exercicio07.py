valorCompra = 0
porcentoDesconto = 0
valorFinal = 0
compraMin = 500
desconto = 0

while True:
    valorCompra = float(input("Digite o valor da compra: "))
    print()
    if valorCompra < compraMin:
        valorFinal = valorCompra
        print(f"O valor da compra é de R${valorCompra:.2f}")
        print(f"Porcentagem de desconto é de R${porcentoDesconto:.2f}")
        print(f"Valor final da compra é de R${valorFinal:.2f}")
    elif valorCompra < 3000:
        for i in range(499, 2999, 100):
            if valorCompra > i:
                porcentoDesconto += 0.01
                desconto = porcentoDesconto * valorCompra
                valorFinal = valorCompra - desconto
        print(f"Valor da compra é de R${valorCompra:.2f}")
        print(f"Porcentagem de desconto é de {porcentoDesconto:.2f}%")
        print(f"Valor do desconto é de R${desconto:.2f}")
        print(f"Valor final da compra é de R${valorFinal:.2f}")
        porcentoDesconto = 0
    elif valorCompra >= 3000:
        porcentoDesconto = 0.25
        desconto = porcentoDesconto * valorCompra
        valorFinal = valorCompra - desconto
        print(f"Valor da compra é de R${valorCompra:.2f}")
        print(f"Porcentagem de desconto é de {porcentoDesconto:.2f}%")
        print(f"Valor do desconto é de R${desconto:.2f}")
        print(f"Valor final da compra é de R${valorFinal:.2f}")
        porcentoDesconto = 0
    else:
        print("Valor inválido. Digite um valor positivo.")
    resposta = input("Deseja calcular o valor de outra compra? (s/n): ")
    print()
    if resposta.lower() != "s":
        print("Encerrando o programa.")
        break
