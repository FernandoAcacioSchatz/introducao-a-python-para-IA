temps = [14.4, 18, 25.3, 4.5, 12.5, 20.1]
maior = temps[0]
soma = 0
for temp in temps:
    soma += temp
    if temp > maior:
        maior = temp

media = sum(temps) / len(temps)
print(f"Maior temperatura: {max(temps)}")
print(f"Menor temperatura: {min(temps)}")
print(f"Média das temperaturas: {media:.2f}")
