numero = int(input("Digite um número: "))
par = []
impar = []
for i in range(1, numero + 1):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

maior = max(len(par), len(impar))
for i in range(maior):
    p = par[i] if i < len(par) else ""
    j = impar[i] if i < len(impar) else " "
    print(f"{p}{j:>6}")
print()
