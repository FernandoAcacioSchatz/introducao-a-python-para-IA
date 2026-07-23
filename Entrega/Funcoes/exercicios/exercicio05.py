def maiorIdade(idade):
    if idade >= 18:
        return True
    else:
        return False


idade = int(input("Digite sua idade: "))
if maiorIdade(idade):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
