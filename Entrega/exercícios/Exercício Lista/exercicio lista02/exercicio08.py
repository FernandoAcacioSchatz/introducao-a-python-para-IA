frutas = ["maçã", "banana", "uva", "laranja", "abacaxi"]


while True:
    search = input("Digite o nome de uma fruta: ").lower()
    if search in frutas:
        print(f"A fruta {search.capitalize()} está na lista.")
    else:
        print(f"A fruta {search.capitalize()} não está na lista.")
