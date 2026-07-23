masc = 0
masNao = 0
fem = 0
femSim = 0
sim = 0
nao = 0
contagem = 0

print("***PESQUISA***")

while contagem < 10:

    sexo = input(f"Digite o sexo da pessoa pessoa (M/F): ").lower()
    if "m" != sexo != "f":
        print(
            "Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino."
        )
    else:
        if sexo == "m":
            masc += 1
        if sexo == "f":
            fem += 1

        resposta = input("Gostou do novo produto? (S/N): ").lower()
        if "s" != resposta != "n":
            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        else:
            if resposta == "s":
                sim += 1
                print("Obrigado por sua resposta!")
            if resposta == "n":
                nao += 1
                print("Obrigado por sua resposta!")

            contagem += 1

    if sexo == "f" and resposta == "s":
        femSim += 1
    if sexo == "m" and resposta == "n":
        masNao += 1


print(f"Total de pessoas que responderam SIM: {sim}")
print(f"Total de pessoas que responderam NÃO: {nao}")
print(f"Total de mulheres que responderam SIM: {femSim}")
print(
    f"Porcebtagem de homens que respondeu NÃO entre todos os homens: {(masNao / masc)* 100}"
)
