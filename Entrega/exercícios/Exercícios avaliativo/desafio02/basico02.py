#########BÁSICO#########
print("Pontuação de Jogo")
pont = float(input("Digite sua pontuação: "))
if pont > 0 and pont < 100:
    print("Nível Iniciante")
elif pont > 100:
    print("Nível Avançado")
else:
    print("Pontuação invalida")
