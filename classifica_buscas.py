#from dados import carregar_buscas
#x, y = carregar_buscas()
# print(x[0])

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
df = pd.read_csv('busca.csv')
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

# Iniciando o treinamento
porcentagem_treino = 0.9
tamanho_de_treino = porcentagem_treino * len(Y)
tamanho_de_teste = len(Y) - tamanho_de_treino


treino_dados = X[:int(tamanho_de_treino)]
treino_marcacoes = Y[:int(tamanho_de_treino)]


teste_dados = X[-int(tamanho_de_teste):]
teste_marcacoes = Y[-int(tamanho_de_teste):]


# Treinando o Algoritmo
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferenças = resultado - teste_marcacoes

acertos = [d for d in diferenças if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)
