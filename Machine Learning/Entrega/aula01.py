import pandas as pd

from sklearn.tree import DecisionTreeClassifier

dados = {
    "horasEstudos": [1, 2, 3, 4, 5, 6],
    "aprovado": [0, 0, 0, 1, 1, 1],
}

# Cria a tabela
df = pd.DataFrame(dados)

# Entradas
x = df[["horasEstudos"]]

# Saídas
y = df["aprovado"]

# Cria o modelo
modelo = DecisionTreeClassifier()

# Treina o modelo
modelo.fit(x, y)

# Nova pessoa
nova_pessoa = [[7]]

# Faz previsão
resultado = modelo.predict(nova_pessoa)


if resultado[0] == 1:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
