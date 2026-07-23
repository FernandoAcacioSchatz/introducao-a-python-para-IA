colegas = ["Maria", "João", "Ana", "Carlos", "Fernanda"]
colegas.append("Pedro")
print(*colegas, sep=", ", end=" \n")

colegas.insert(2, "Otávio")
print(*colegas, sep=", ", end=" \n")

colegas.remove("João")
print(*colegas, sep=", ", end=" \n")
colegas.sort()
print(*colegas, sep=", ", end=" ")
