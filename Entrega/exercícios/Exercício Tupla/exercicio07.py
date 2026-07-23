nomes = (
    "Maria",
    "João",
    "Pedro",
    "Ana",
    "Lucas",
    "Carla",
    "Rafael",
    "Fernanda",
    "Gustavo",
    "Juliana",
)

while True:
    search = input("Digite um nome para buscar: ").capitalize()
    if search in nomes:
        print(f"O nome {search} está na lista.")
    else:
        print(f"O nome {search} não está na lista.")
