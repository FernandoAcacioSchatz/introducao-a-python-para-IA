media = 0
idades = []
while True:
    idade = int(input("Digite a idade: "))
    if idade == 0:
        break
    elif 1 <= idade >= 120:
        break
    else:
        idades.append(idade)
        media = sum(idades) / len(idades)
if media > 0:
    print(f"A média das idades até agora é: {media:.2f}")
else:
    print("Nenhuma idade válida foi inserida.")
