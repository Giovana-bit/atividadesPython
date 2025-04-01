#Exercício 1 - Argumentos Padrão
def contaPalavras(texto, separador= " "):
    return len (texto.split(separador))

#Exercício 2 - Funções Lambda
numeros = {1, 2, 3, 4, 5}
quadros = pares=list(filter(lambda X: X**2, numeros))

#Exercício 3 - Recursão
def fibonacci(n):
    if n <= 0:
        return "Inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#Resultados
textoExemplo = "Teste 01"
print(f"Números de palavras: {contaPalavras(textoExemplo)}")

print(f"Quadrados da lista: {quadros}")

n = 7
print(f"{n}° termo da squencia fibonacci: {fibonacci(n)}")