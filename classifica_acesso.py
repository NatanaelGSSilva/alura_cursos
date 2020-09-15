from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB


x, y = carregar_acessos()

modelo = MultinomialNB()
modelo.fit(x, y)

misterioso = [1, 0, 1]
misterioso2 = [1, 0, 0]
misterioso2 = [1, 0, 0]
print(modelo.predict([misterioso, misterioso2]))
