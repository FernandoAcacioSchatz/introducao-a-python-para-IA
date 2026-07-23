lista = []


def cadastrarProduto():
    while True:
        produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
        if produto.lower() == "sair":
            listarProduto()
            break
        lista.append(produto)


def listarProduto():
    print("\n--- Lista de Produtos ---")
    for produto in lista:
        print(f"- {produto}")


cadastrarProduto()
