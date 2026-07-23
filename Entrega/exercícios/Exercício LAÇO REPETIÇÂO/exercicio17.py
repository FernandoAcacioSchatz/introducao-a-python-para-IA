pessoasMais90 = 0
somaIdade = 0
contador = 1
quant = 2
lista = []
mediaIdade = 0

for i in range(quant):
    idade = int(input(f"Digite a idade da {contador}° pessoa: "))
    contador += 1
    lista.append(idade)
    somaIdade += idade

    if idade > 90:
        pessoasMais90 += 1

mediaIdade = somaIdade / len(lista)
for item in lista:
    contador = 1
    print(f"Idade: {item} da {contador}° pessoa")
    contador += 1
print(f"A quantidade de pessoas com mais de 90 anos é de {pessoasMais90}")
print(f"A média de idade das pessas é de {mediaIdade:.0f}")
