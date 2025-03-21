#Exercício 3 - Dicionários
# a) Aplicar desconto de 10% em produtos com preço superior a 100
produtos = {"celular": 1500, "fone": 80, "notebook": 2500, "mouse": 50}

for produto, preco in produtos.items():
    if preco > 100:
        produtos[produto] = preco * 0.9  # Aplicando 10% de desconto

print("Preços atualizados:", produtos)

# b) Criar um dicionário para armazenar informações de um livro
livro = {"título": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899}

if livro["ano"] > 2000:
    print("O livro foi publicado depois de 2000.")
else:
    print("O livro foi publicado antes ou em 2000.")