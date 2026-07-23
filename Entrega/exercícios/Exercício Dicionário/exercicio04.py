pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa)
print(
    "Nome:",
    pessoa["nome"],
    ", Idade:",
    pessoa["idade"],
    ", Cidade:",
    pessoa["cidade"],
)

pessoa["idade"] = 45
print(
    "Nome:",
    pessoa["nome"],
    ", Idade:",
    pessoa["idade"],
    ", Cidade:",
    pessoa["cidade"],
)


pessoa["Profissão"] = "Programador"
print(
    "Nome:",
    pessoa["nome"],
    ", Idade:",
    pessoa["idade"],
    ", Cidade:",
    pessoa["cidade"],
    ", Profissão:",
    pessoa["Profissão"],
)
print()
for chave, valor in pessoa.items():
    print(chave, ":", valor)
