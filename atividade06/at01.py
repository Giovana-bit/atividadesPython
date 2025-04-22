#Criando e escrevendo no arquivo
with open('poema.txt', 'w') as arquivo:
    arquivo.write ("No meio do caminho tinha uma pedra \nTinha uma pedra no meio do caminho")

#Lendo o arquivo
with open('poema.txt', 'r') as arquivo:
    print(arquivo.read())