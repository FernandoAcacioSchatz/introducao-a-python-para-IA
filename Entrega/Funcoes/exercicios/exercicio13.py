def converterParaMaiusculo(texto):
    return texto.upper()


texto = input("Digite um texto para converter para maiúsculas: ")
texto_maiusculo = converterParaMaiusculo(texto)
print(f"Texto em maiúsculas: {texto_maiusculo}")
