frutas = {"banana", "maçã", "uva", "abacaxi"}
print(*map(str.capitalize, frutas), sep=", ", end=".\n")
print()
frutas.add("laranja")
print(*map(str.capitalize, frutas), sep=", ", end=".\n")
print()
frutas.discard("banana")
print(*map(str.capitalize, frutas), sep=", ", end=".\n")


print(
    "A uva está presente no conjunto de frutas."
    if "uva" in frutas
    else "A uva não está presente no conjunto de frutas."
)
