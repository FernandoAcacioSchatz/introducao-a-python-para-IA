a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("União:", *map(str, a | b), sep="\n", end="\n")
print("Interseção:", *map(str, a & b), sep="\n", end="\n")
print("Diferença:", *map(str, a - b), sep="\n", end="\n")
print("Diferença:", *map(str, b - a), sep="\n", end="\n")
