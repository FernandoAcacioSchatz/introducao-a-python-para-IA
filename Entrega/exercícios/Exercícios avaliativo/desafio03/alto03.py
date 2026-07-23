vip = input("Você é um cliente VIP? (S/N): ").lower()
print("Informe o qnt e o valor dos produtos")
qnt1 = float(input("Digite o qnt do 1° produto: "))
valor1 = float(input("Digite o valor do 1° produto: "))
print()
qnt2 = float(input("Digite o qnt do 2° produto: "))
valor2 = float(input("Digite o valor do 2° produto: "))
print()
qnt3 = float(input("Digite o qnt do 3° produto: "))
valor3 = float(input("Digite o valor do 3° produto: "))
print()
qnt4 = float(input("Digite o qnt do 4° produto: "))
valor4 = float(input("Digite o valor do 4° produto: "))
print()
qnt5 = float(input("Digite o qnt do 5° produto: "))
valor5 = float(input("Digite o valor do 5° produto: "))
print()
if (
    qnt1 < 0
    or valor1 < 0
    or qnt2 < 0
    or valor2 < 0
    or qnt3 < 0
    or valor3 < 0
    or qnt4 < 0
    or valor4 < 0
    or qnt5 < 0
    or valor5 < 0
):
    print("Valor ou quantidade inválida, tente novamente")
soma = (
    (qnt1 * valor1)
    + (qnt2 * valor2)
    + (qnt3 * valor3)
    + (qnt4 * valor4)
    + (qnt5 * valor5)
)
porcento = 0
desconto = 0
valorFinal = 0
porcentoVip = 0.05

if soma >= 100 and soma < 200:
    porcento = 0.10
    if vip == "s":
        valorFinal = valorFinal - (valorFinal * porcentoVip)
        porcento = porcento + porcentoVip
    desconto = soma * porcento
    valorFinal = soma - desconto
    print(
        f"O valor de sua compra é de R${soma:.2f}, seu desconto é de R${desconto:.2f} e o valor final é de R${valorFinal:.2f} "
    )
elif soma >= 200:
    porcento = 0.20
    if vip == "s":
        valorFinal = valorFinal - (valorFinal * porcentoVip)
        porcento = porcento + porcentoVip

    desconto = soma * porcento
    valorFinal = soma - desconto
    print(
        f"O valor de sua compra é de R${soma:.2f}, seu desconto é de R${desconto:.2f} e o valor final é de R${valorFinal:.2f} "
    )
else:
    valorFinal = soma
    if vip == "s":
        valorFinal = valorFinal - (valorFinal * porcentoVip)
    print(
        f"O valor de sua compra é de R${valorFinal:.2f} e o valor do desconto é de R${soma - valorFinal:.2f}"
    )
