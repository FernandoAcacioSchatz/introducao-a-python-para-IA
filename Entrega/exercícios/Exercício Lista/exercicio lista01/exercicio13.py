numeros = [9, 2, 7, 1, 5]
print("Ordem inserida: ", *numeros, sep=" ", end="\n")
numeros.sort(reverse=True)
print("Ordem decrescente: ", *numeros, sep=" ", end="\n")
numeros.sort()
print("Ordem crescente: ", *numeros, sep=" ", end="\n")
