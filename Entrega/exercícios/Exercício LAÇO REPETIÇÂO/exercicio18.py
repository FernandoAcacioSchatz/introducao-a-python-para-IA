# 1. Inicia o dicionário vazio FORA do for
pessoas = {}
listaNomes = []
idade50Peso60 = 0
somaIdadeAlt150 = 0
contadorAlt150 = 0
ruivaNãoOlhosAzuis = 0
contadorAzuis = 0
contadorRuiva = 0


for i in range(2):
    while True:
        nome = input(f"Digite o nome da {i+1}ª pessoa: ").strip().title()

        nome_tratado = nome.replace(" ", "").replace("-", "")

        if nome_tratado.isalpha():
            break
        else:
            print("Digite apenas letras!")

    listaNomes.append(nome)
    idade = int(input(f"Digite a idade de {nome}: "))
    while True:
        if idade > 1 or idade < 115:
            peso = float(input(f"Digite o peso de {nome} (em kg): "))
            if peso < 0 or peso > 500:
                print("Digite o peso novamente")
            else:
                altura = float(input(f"Digite a altura de {nome} (em metros): "))
                corOlho = (
                    input(
                        f"Qual a cor do seus olhos. Digite A para Azul, P para Preto, V para Verde, C para Castanho: "
                    )
                    .strip()
                    .lower()
                )
                if corOlho == "a":
                    contadorAzuis += 1
                if (
                    corOlho != "a"
                    and corOlho != "p"
                    and corOlho != "v"
                    and corOlho != "c"
                ):
                    print("Digite a cor do olho novamente")
                else:
                    corCabelo = (
                        input(
                            f"Qual a cor do seu cabelo. Digite P para Preto, C para Castanho, L para Louro, R para Ruivo: "
                        )
                        .strip()
                        .lower()
                    )
                    if (
                        corCabelo != "p"
                        and corCabelo != "c"
                        and corCabelo != "l"
                        and corCabelo != "r"
                    ):
                        print("Digite a cor do cabelo novamente")
                    else:
                        pessoas[nome] = {
                            "idade": idade,
                        }

        if idade > 50 and peso < 60:
            idade50Peso60 += 1

        if altura < 1.50:
            somaIdadeAlt150 += idade
            contadorAlt150 += 1

        if corCabelo == "r" and corOlho != "a":
            ruivaNãoOlhosAzuis += 1
        else:
            print("Você esta vivo? Digite a idade novamente")
            break

porcentagem = (contadorAzuis / len(listaNomes)) * 100
mediaIdadeAlt150 = somaIdadeAlt150 / contadorAlt150

print(len(listaNomes))
print()
print()
print(f"{idade50Peso60} pessoas tem mais de 50 anos e peso inferior a 60 kg")
print(
    f"A média de idade das pessoas com altura inferior a 1.50m é de {mediaIdadeAlt150:.0f} anos"
)
print(f"{ruivaNãoOlhosAzuis} pessoas são ruivas e não tem olhos azuis")
print(f"A porcentagem de pessoas com olhos azuis é de {porcentagem:.2f}%")
print()
