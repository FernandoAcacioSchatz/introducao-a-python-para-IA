palavra = input("Digite qualquer palavra: ")
letras = set(palavra)
print(*map(str, letras), sep=", ", end=".\n")
