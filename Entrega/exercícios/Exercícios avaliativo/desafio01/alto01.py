#########ALTO#########
print("**Laboratório**")

horas = int(input("Digite as horas: "))
if horas > 23:
    print("Hora invalida, recomece")
else:
    minutos = int(input("Digite os minutos: "))
    if minutos > 59:
        print("Minutos invalidos, recomece")
    elif horas >= 22:
        print("Entrada negada após as 22 horas")
    else:
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
