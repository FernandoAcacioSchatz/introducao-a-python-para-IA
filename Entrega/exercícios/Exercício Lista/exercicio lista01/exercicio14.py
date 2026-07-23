numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = sum(num for num in numeros if num % 2 != 0)
print(*numeros, sep=", ", end=".\n")
print(f"A soma dos números ímpares da lista é de {soma}")
