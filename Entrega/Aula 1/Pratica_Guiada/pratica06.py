print("=== Programa de Apresentação ===")

nome = input("Seu nome: ").capitalize()
ano_nasc = int(input("Ano de nascimento: "))
cidade = input("Cidade natal: ").capitalize()


idade = 2026 - ano_nasc
ano_100 = ano_nasc + 100

print(f"\nOlá, {nome}!")
print(f"Você tem {idade} anos e nasceu em {cidade}.")
print(f"Em {ano_100} você completará 100 anos!")
