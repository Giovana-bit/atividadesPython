#Funções

def saudacao():
    print("Olá, seja bem-vinda!")
saudacao() #Chama a função saudação

#Parâmetros e argumentos
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vinda")
saudacao("Giovana") #Saída com o nome

#Com múltiplos parâmetros
def soma(a, b):
    return a + b

resultado = soma(5, 3) #Passa 5 e 3 como argumentos
print(resultado) #Saída com o resultado da soma

#Retorno de valores
def multiplica(a, b):
    return a * b

resultado = multiplica(4, 5)
print(resultado) #Saída com o resultado da multiplicação

#Retorno de valores como uma tupla
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

resultadoSoma, resultadoSubtracao = operacoes(10, 5)
print(resultadoSoma)
print(resultadoSubtracao)

#Escopo de variáveis
def minhaFuncao():
    x = 10 #Var9ável local
    print(x)
minhaFuncao() #Exibir o 10
#print(x) #Causaria um erro, pois não e visivel fora da função

x = 20 #Variavel local
def minhaFuncao():
    print(x) #Acessar a variavel global

minhaFuncao()

X = 10
def minhaFuncao():
    global x
    x = 20

minhaFuncao()
print(x) #Saída 20(variavel local foi modificada)

#Argumentos padrão
def saudacao(nome, mensagem="Olá!"):
    print(f"{mensagem}, {nome}")

saudacao("Giovana") #Saída com o "Olá" + nome
saudacao("Samuel", "Bom dia!") #Saída "Bom dia" + nome

#Argumentos Posicionais e Nomeados
def exibirInfo(nome, idade):
    print(f"Nome: {nome}, Idade:{idade}")

exibirInfo("Giovana", 18) #Argumentos pisicionais
exibirInfo(idade=19, nome="Samuel") #Argumentos nomeados

#Funções anônimas(Lambda)
soma = lambda a, b: a + b
print(soma(3, 4)) #Sair resultado da soma

numeros={1, 2, 3, 4, 5, 6,}
pares=list(filter(lambda X: X%2 == 0, numeros))
print(pares) #Saída 2, 4, 6

#Funções como Objetos de Primeira Classe
def somar(a, b):
    return a + b

def executarFuncao(func, a, b):
    return func(a, b)

resultado = executarFuncao(somar, 5, 3)
print(resultado)

#Funções Recursivas
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5)) #Saída 120