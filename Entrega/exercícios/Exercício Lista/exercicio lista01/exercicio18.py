numeros = [float(input(f"Digite o {i +1}° número: ")) for i in range(10)]

print(f" {', '.join(map(str,set(numeros)))}")
