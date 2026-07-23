idade = []
masc = []
femi = []
for i in range(7):
    id = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    idade.append(id)
    if sexo == "M":
        masc.append(id)
    elif sexo == "F":
        femi.append(id)
media_idade = sum(idade) / len(idade)
media_masc = sum(masc) / len(masc)
if len(masc) == 0:
    media_masc = 0
media_femi = sum(femi) / len(femi)
if len(femi) == 0:
    media_femi = 0
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Média de idade dos homens: {media_masc:.2f}")
print(f"Média de idade das mulheres: {media_femi:.2f}")
