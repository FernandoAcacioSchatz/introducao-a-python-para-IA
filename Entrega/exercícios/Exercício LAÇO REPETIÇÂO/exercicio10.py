idadePessoas = []
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
idade = 0
for i in range(15):
    idade = int(input("Digite a sua idade: "))
    if idade >= 1 and idade <= 15:
        faixa1 += 1
    elif idade > 15 and idade <= 30:
        faixa2 += 1
    elif idade > 30 and idade <= 45:
        faixa3 += 1
    elif idade > 45 and idade <= 60:
        faixa4 += 1
    elif idade > 60 and idade <= 115:
        faixa5 += 1
    else:
        break
if idade < 1 or idade > 115:
    print("Idade invalida, recomeçe")
else:
    print(
        f"No grupo tem {faixa1} pessoas com idade entre 1 e 15 anos, {faixa2} pessoas com idade entre 16 e 30 anos, {faixa3} pessoas com idade entre 31 e 45 anos, {faixa4} pessoas com idade entre 46 e 60 anos e {faixa5} pessoas com idade acima de 60 anos."
    )
