catalogo = [
    {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "categoria": "Romance",
        "paginas": 256,
        "disponivel": True,
    },
    {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "categoria": "Fantasia",
        "paginas": 1178,
        "disponivel": False,
    },
    {
        "titulo": "Clean Code",
        "autor": "Robert C. Martin",
        "categoria": "Tecnologia",
        "paginas": 431,
        "disponivel": True,
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "categoria": "Tecnologia",
        "paginas": 328,
        "disponivel": False,
    },
    {
        "titulo": "O Guia do Mochileiro",
        "autor": "Douglas Adams",
        "categoria": "Fantasia",
        "paginas": 224,
        "disponivel": False,
    },
]
listaDisponivel = []
totalPaginas = 0
listaNomes = []
categorias = {}

for produto in catalogo:
    categoria = produto["categoria"]
    if categoria in categorias:
        categorias[categoria] += 1
    else:
        categorias[categoria] = 1


for produtos in catalogo:
    totalPaginas += produtos["paginas"]
    listaNomes.append(produtos["titulo"])
    if produtos["disponivel"] == True:
        listaDisponivel.append(produtos["titulo"])


nome = input("Digite o título do livro que deseja buscar: ").strip().lower()

for produto in catalogo:

    if produto["titulo"].lower() == nome:
        if produto["disponivel"]:
            print(f"Produto encontrado: {produto['titulo']}")
            print("Disponível")
        else:
            print(f"Produto encontrado: {produto['titulo']}")
            print("Indisponível")

        break
else:
    print("Livro não encontrado.")

for categoria, quantidade in categorias.items():
    print(f"Categoria: {categoria} - Quantidade: {quantidade}")

print("***LIVROS DISPONÍVEIS***")
print(listaNomes)
print(listaDisponivel)
print(totalPaginas)
