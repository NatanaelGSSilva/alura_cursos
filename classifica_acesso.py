from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB


x, y = carregar_acessos()

treino_dados = x[:90]
treino_marcacoes = y[:90]

teste_dados = x[-9:]
teste_marcacoes = y[-9:]


modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
# resultado é o que eu previ -y é o valor real
diferenças = resultado - teste_marcacoes

acertos = [d for d in diferenças if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)
print(total_de_elementos)
