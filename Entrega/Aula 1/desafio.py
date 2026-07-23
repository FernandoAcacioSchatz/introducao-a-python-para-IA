print("Caixa Registradora")
nome = input("Digite o nome do cliente: ")
nomeItem1 = input("Digite o nome do primeiro item: ")
qtItem1 = int(input("Digite a quantidade do primeiro item: "))
valor1 = float(input("Digite o valor do primeiro item: "))
somaItem1 = qtItem1 * valor1
nomeItem2 = input("Digite o nome do segundo item: ")
qtItem2 = int(input("Digite a quantidade do segundo item: "))
valor2 = float(input("Digite o valor do segundo item: "))
somaItem2 = qtItem2 * valor2
nomeItem3 = input("Digite o nome do terceiro item: ")
qtItem3 = int(input("Digite a quantidade do terceiro item: "))
valor3 = float(input("Digite o valor do terceiro item: "))
somaItem3 = qtItem3 * valor3
valorTotal = somaItem1 + somaItem2 + somaItem3
desconto = valorTotal * 0.10
valorFinal = valorTotal - desconto
print(
    f"\nO cliente {nome} comprou. \n{nomeItem1}  {qtItem1}\n{nomeItem2}  {qtItem2}\n{nomeItem3}  {qtItem3}."
)
print(
    f"O valor total da compra é R$ {valorTotal:.2f}\nO valor do desconto é R$ {desconto:.2f}\nO valor final a ser pago é R$ {valorFinal:.2f}."
)
