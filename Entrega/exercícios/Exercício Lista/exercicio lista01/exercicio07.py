from statistics import mean

notas = [float(input(f"Digite a {i +1}° nota: ")) for i in range(5)]

print()
print(f"A média das notas é: {mean(notas)}")
