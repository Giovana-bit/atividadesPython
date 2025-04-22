while True:
    citacao = input("Digite sua citação favorita(ou 'sair' para encerrar):")
    if citacao.lower() == 'sair':
        break
    with open('citacoes.txt', 'a') as arquivo:
        arquivo.write(citacao + "\n")