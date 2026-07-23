temp = float(input("Digite a temperatura em Celsius: "))
pressao = int(input("Digite a pressão sistólica: "))
dor = int(input("Digite o nivel de dor (0 a 10): "))

if temp > 39.5 or pressao > 180 or dor >= 9:
    cor = "Vermelho (Emergência)"
elif temp > 38.5 or pressao > 160 or dor >= 7:
    cor = "Laranja (Muito Urgente)"
elif temp > 37.5 or pressao > 140 or dor >=4:
    cor = "Amarelo (Urgente)"
else:
    cor = "Verde (Pouco Urgente)"

print(f"{cor}")
