nomes = ["Maria", "João", "Ana", "Carlos", "Beatriz"]
print(*nomes, sep=", ", end=".\n")
print()
nomes.append("Fernanda")
print(*nomes, sep=", ", end=".\n")
print()
nomes.remove("Carlos")
print(*nomes, sep=", ", end=".\n")
