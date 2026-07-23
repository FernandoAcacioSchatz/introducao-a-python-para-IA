import random

secreto = random.randint(1, 100)


tentativas = 0
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite == secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < secreto:
        print("Baixo. Tente novamente.")
    else:
        print("Alto. Tente novamente.")
    if tentativas >= 5:
        print("Você excedeu o número de tentativas")
        break
