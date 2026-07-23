compVista = []
compPrazo = []
juros = 0.10
lista = []
quantCompra = 5

for i in range(quantCompra):
    compra = input("Digite 'V' para compra a vista e 'P' para compra a prazo: ").lower()
    if compra == "v":
        print("\nCompra a vista.")
        compVista.append(float(input("Digite o valor da compra a vista: ")))
        lista.append("v")
        print()
    elif compra == "p":
        print("\nCompra a prazo.")
        compPrazo.append(float(input("Digite o valor da compra a prazo: ")))
        lista.append("p")
        print()
    else:
        break
if len(lista) == quantCompra:
    print(f"Valor total das compras a vista: R$, {sum(compVista)}")
    print(f"Valor total das compras a prazo: R$ {sum(compPrazo) * (1 + juros):.2f}")
    print(
        f"Valor total das compras: R$ {sum(compVista) + sum(compPrazo) * (1 + juros):.2f}"
    )
else:
    print("Digito inválido, recomece")
