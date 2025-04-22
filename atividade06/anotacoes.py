#Abrindo e Fechando Arquivos
arquivo = open('arquivo.txt', 'modo')
#....Operações com o arquivo
arquivo.close()

#Garantir que o arquivo seja fechado adequadamente
#with open('arquivo.txt', 'modo') as arquivo:

#Lendo arquivos
#Ler o arquivo inteiro:
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Ler linha por linha
with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

#Escrevendo em arquivos
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write("Escrevendo uma linha no arquivo. \n")
    arquivo.write("Escrevendo outra linha")

#Usando a para adicionar conteúdo
with open('arquivo.txt', 'a') as arquivo:
    arquivo.write("\n Adicionando mais uma linha")

#Arquivo CSV (Comma-Separated Values)
#Exemplo de Leitura
import csv
with open('arquivo.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

#Exemplo de Escrita
import csv
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Giovana', 18, 'São Paulo'],
    ['Samuel', 19, 'Curitiba']
]

with open('arquivo.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)