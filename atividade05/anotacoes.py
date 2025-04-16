#Módulos
#Importando módulos
import math

resultado = math.sqrt(16)
print(resultado) #Saída: 4.0

#Importando Funções Específicas de um Módulo
from math import sqrt, pi

print(sqrt(25)) #Saida 5.0
print(pi) #3.141592653589793

#Importando com Alias
import math as m

print(m.sqrt(9)) #Saída 3.0

#Criando próprios Módulos (Mesmo código na pasta meuModulo.py)
def saudacao(nome):
    return F"Olá, {nome}!"

def soma (a, b):
    return a + b

import meuModulo

print(meuModulo.saudacao("Gi")) #Saída: Olá, Gi!
print(meuModulo.soma(10,5)) #Saída 15

#Explorando Módulos Padrão
import os
print(os.getcwd()) #Retorna o diretório atual

#Módulos Externos
#Código no CMD  (pip install requests)
import requests

reposta = requests.get('https://api.github.com')
print(reposta.status_code) #Saída 200 (se a solicitação for bem-sucedida)

#Introduções a Exeções
#ZeroDivisionError: Tentativa de dividir por zero
#TypeError: Operação em tipos de dados incompatíveis
#ValueError: Valor incorreto passado para uma função
#FileNotFoundError: Tentativa de acessar um arquivo que não existe
#IndexError: Tentativa de acessar um índice fora do intervalo de uma lista

#Bloco try e except 
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro: entrada inválida, por favor digite um número.")

#Bloco Else
try:
    numero = int(input("Digite um número"))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro: entrada onválida, por favor digite um número.")
else:
    print(f"Resultado: {resultado}")

#Bloco finally
try: 
    arquivo = open('dados.txt', 'r')
    conteudo = arquivo.read()
except FileExistsError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    arquivo.close()
    print("O arquivo foi fechado.")

#Levantamento Execões com raise
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Erro: {e}")

#Criando Exeções Personalizadas
class saldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo insuficiente: Saldo atual é {saldo}, mas tentou sacar {valor}.")
    
def sacar(saldo, valor):
    if valor > saldo:
        raise saldoInsuficienteError(saldo, valor)
    saldo -= valor
    return saldo
try:
    saldoAtual = sacar (100, 150)
except saldoInsuficienteError as e:
    print(e) 