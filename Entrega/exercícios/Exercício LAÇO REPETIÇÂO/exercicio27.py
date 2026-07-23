otimo = []
bom = []
regular = []
qnt = 15
idadeEspec = []
for i in range(qnt):
    idadeEspec.append(int(input("Digite sua idade: ")))
    while idadeEspec[i] < 1 or idadeEspec[i] > 115:
        print("Idade inválida, tente novamente.")
        idadeEspec[i] = int(input("Digite sua idade: "))
        if idadeEspec[i] >= 1 and idadeEspec[i] <= 115:
            while opiniao in ["3", "2", "1"]:
                opiniao = input(
                    "Digite sua opinião (Ótimo = 3, Bom = 2 ou Regular = 1): "
                )
                if opiniao == "3":
                    otimo.append(idadeEspec[i])
                elif opiniao == "2":
                    bom.append(idadeEspec[i])
                elif opiniao == "1":
                    regular.append(idadeEspec[i])
                else:
                    print("Opção inválida, tente novamente.")
                    opiniao = input(
                        "Digite sua opinião (Ótimo = 3, Bom = 2 ou Regular = 1): "
                    )
