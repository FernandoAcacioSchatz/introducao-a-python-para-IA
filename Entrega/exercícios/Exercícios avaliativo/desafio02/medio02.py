#########MEDIO#########
print("Pontuação de Jogo")
pont = float(input("Digite sua pontuação: "))
if pont > 0 and pont < 100:
    print("Nível Iniciante")
elif pont >= 100 and pont < 200:
    print("Nível Intermediário")
elif pont >= 200:
    print("Nível Elite")
else:
    print("Pontuação invalida")
