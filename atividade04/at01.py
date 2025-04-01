#Exercício 1 - Função saudadação
def saudacao(nome):
    print(f"Boa noite {nome}, muito bem-vindo(a)")

#Exercício 2 - Soma e Produto
def somaProduto(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

#Exercício 3 - Função com Escopo Local
def funcaoComVariavelLocal():
    variavelLocal = "Testando variavel local"
    print(variavelLocal)

#Resultados
saudacao("Thamires")

soma, produto = somaProduto(6, 3)
print(f"Soma {soma}, Produto: {produto}")

funcaoComVariavelLocal()