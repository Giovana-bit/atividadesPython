import csv
dados = [
    ['Nome', 'Idade', 'Nota'],
    ['Ana', 20, 9],
    ['Giovana', 18, 10],
    ['Samuel', 19, 8],
    ['Victor', 21, 7]
]

#Escrevendo dados
with open('alunos.csv', 'a', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
#Lendo os dados
with open('alunos.csv', 'r') as arquivo:
    leitor=csv.reader(arquivo)
    for linha in leitor:
        print(linha)