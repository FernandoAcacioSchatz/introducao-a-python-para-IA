lista = []
while True:
    numero = float(input("Digite um número ou 0 para sair: "))
    if numero == 0:
        break
    lista.append(numero)
print()
print(f"Maior valor: {max(lista)}")
print(f"Menor valor: {min(lista)}")
