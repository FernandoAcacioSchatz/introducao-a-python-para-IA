# Verificador de senha com NOT
senha_correta = "python123"
senha_digitada = input("Digite a senha: ")
if not senha_digitada == senha_correta:
    print("Senha incorreta")
else:
    print("Senha correta")

senha_admin = "admon123"
senha_usuario = input("Digite a senha: ")
if senha_usuario != senha_admin:
    print("Acesso negado")
else:
    print("Acesso concedido")
