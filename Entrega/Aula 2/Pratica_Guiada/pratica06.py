# Caixa registradora com desconto
valorTotal = float(input("Digite o valor total da compra:"))
if valorTotal > 100:
    desconto = valorTotal * 0.15
elif valorTotal > 50:
    desconto = valorTotal * 0.10
else:
    desconto = 0
valorFinal = valorTotal - desconto
print(
    f"O valor da compra é R${valorTotal:.2f}\nDesconto aplicado: R${desconto:.2f}\n Valor final da compra: R${valorFinal:.2f}"
)
