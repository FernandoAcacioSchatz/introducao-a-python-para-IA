lado = int(input("Digite o lado do quadrado: "))
esp = " "
if lado <= 0 or lado > 20:
    print("O lado do quadrado deve ser um número positivo e menor ou igual a 20.")
else:
    for i in range(lado):
        print("*" * lado)
        break
    for i in range(lado - 2):
        print("*" + esp * (lado - 2) + "*")
    for i in range(lado):
        print("*" * lado)
        break

print()
