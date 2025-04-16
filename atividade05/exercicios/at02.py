import os 
print("Diretório atual:", os.getcwd())

itens = os.listdir()
for item in itens:
    print(item)

os.mkdir("Novo diretório")
print("Diretório: 'novo_diretorio' criado com sucesso!")