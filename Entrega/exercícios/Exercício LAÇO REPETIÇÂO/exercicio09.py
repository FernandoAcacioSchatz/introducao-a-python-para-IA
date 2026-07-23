idadePessoa = []
maior18 = 0
menor18 = 0
idade = 0
for i in range(3):
    idade = int(input("Digite a sua idade: "))
    idadePessoa.append(idade)
    if idade >= 1 and idade < 18:
        menor18 += 1
    elif idade > 18:
        maior18 += 1
    else:
        break
if idade < 1:
    print("Idade invalida, recomeçe")
else:
    print("idades digitadas:", end=" ")
    print(*idadePessoa, sep=", ", end=".\n")
    print(f"No grupo tem {maior18} com 18 anos ou mais e {menor18} menores de idade")
