num = [2, 4, -1, 5, 11, -43, 4, -2, 0, 3]
print(*num, sep=", ", end=".\n\n")
num.sort()
print(*num, sep=", ", end=".\n\n")
num.sort(reverse=True)
print(*num, sep=", ", end=".\n\n")
