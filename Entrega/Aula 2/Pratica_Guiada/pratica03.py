# Operadores lógicos OR e AND
idade = int(input("Digite sua idade: "))
tem_autorizacao = input("Você tem autorização dos pais? (sim/não): ").lower() == "sim"
if idade >= 18 and tem_autorizacao:
    print("Pode entrar na festa.")
else:
    print("Não pode entrar na festa")
estutante = input("Você é um estudante? (sim/não): ").lower() == "sim"
idoso = input("Você é idoso? (sim/não): ").lower() == "sim"
if estutante or idoso:
    print("Você tem direito a desconto.")
else:
    print("Você não tem direito a desconto.")
