while True:
    print()
    num = int(input("Digite um número inteiro ou ZERO pra sair: "))
    tab = num
    if tab == 0:
        break
    if tab >= 0:
        for i in range(1, 11):
            print(f"{i} * {tab} = {i * tab}")
    else:
        print("Digite um número inteiro positivo.")
        tab = int(input("Digite um número inteiro: "))
