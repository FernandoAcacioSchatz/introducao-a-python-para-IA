lado = int(input("Digite o lado do quadrado: "))
if lado <= 0 or lado > 20:
    print("O lado do quadrado deve ser um número positivo e menor ou igual a 20.")
else:
    for i in range(lado):
        print("*  " * lado)
print()
