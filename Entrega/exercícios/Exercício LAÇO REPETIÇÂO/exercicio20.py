media = 0
pesoMais90AlturaMenos150 = 0
mede190DezTrinta = 0
idade = []


for i in range(10):
    idade.append(int(input("Digite a sua idade: ")))
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    if peso > 90 and altura < 1.50:
        pesoMais90AlturaMenos150 += 1
    if altura > 1.90 and 10 <= idade[i] <= 30:
        mede190DezTrinta += 1

media = sum(idade) / len(idade)

print(f"A média da idade das {len(idade)} pessoas é: {media}")
print(
    f"A porcentagem de pessoas com peso superior a 90 kg e altura inferior a 1.50 m é: {(pesoMais90AlturaMenos150 / len(idade)) * 100:.2f}%"
)
