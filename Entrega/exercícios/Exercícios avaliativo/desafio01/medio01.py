#########MÉDIO#########
print("**Laboratório**")
idade = int(input("Digite sua idade: "))
if idade < 1 or idade > 105:
    print("Você está vivo?")
elif idade < 16:
    print("Idade inferior ao permitido")
    print("Entrada negada")
elif idade >= 18:
    print("Entrada permitida")
else:
    auturizacao = input(
        "Você está autorizado? Digite S para sim e N para não: "
    ).lower()
    if auturizacao == "s":
        print("Entrada permitida com autorização")
    elif auturizacao == "n":
        print("Entrada negada")
    else:
        print("Digito invalido. Recomece")
