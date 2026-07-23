fatorial = 1
listaNumeros = []
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    numero = int(entrada)

    for i in range(numero, 0, -1):
        fatorial = fatorial * i
        listaNumeros.append(str(i))
    print(f"{' x '.join(listaNumeros)} = {fatorial}")
