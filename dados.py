import csv


def carregar_acessos():
    x = []
    y = []

    arquivo = open("acessos.csv", "r")

    leitor = csv.reader(arquivo)

    # leitor.next()

    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:

        x.append([acessou_home, acessou_como_funciona, acessou_contato])

        y.append(comprou)

    return x, y


# from dados import carregar_acessos importar a funcao carregar acessos de dados.py
# x, y = carregar_acessos() vou rodar a minha função
# marcacoes
# dados
