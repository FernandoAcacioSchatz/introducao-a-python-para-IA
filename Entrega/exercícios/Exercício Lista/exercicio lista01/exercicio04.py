frutas = ["maçã", "banana", "uva", "laranja"]
print(*frutas, sep=", ", end=".\n")
frutas.remove("banana")
print(*frutas, sep=", ", end=".\n")
