import csv


def carregar_acessos():
    x = []
    y = []

    arquivo = open("acessos.csv", "r")

    leitor = csv.reader(arquivo)

    next(leitor)

    for home, como_funciona, \
            contato, comprou in leitor:

        dado = ([int(home), int(
            como_funciona), int(contato)])

        x.append(dado)
        y.append(int(comprou))

    return x, y


def carregar_buscas():
    x = []
    y = []

    arquivo = open("busca.csv", "r")
    leitor = csv.reader(arquivo)
    next(leitor)  # ignorar a primeira linha

    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado)]

        x.append(dado)
        y.append(int(comprou))
    return x, y

# print(carregar_acessos())

# from dados import carregar_acessos importar a funcao carregar acessos de dados.py
# x, y = carregar_acessos() vou rodar a minha função
# marcacoes
# dados
