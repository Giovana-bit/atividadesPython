#Tipos de Variáveis
x = 10  # Variável global

class Exemplo:
    y = 20  # Variável de classe

    def __init__(self):
        self.z = 30  # Variável de instância

    def acessar_variaveis(self):
        w = 40  # Variável local
        print("Variável global x:", x)
        print("Variável de classe y:", Exemplo.y)
        print("Variável de instância z:", self.z)
        print("Variável local w:", w)

print("Acessando a variável global x fora da classe:", x)

#Método de Instância
class Exemplo:
    def metodo_instancia(self):
        print("Este é um método de instância.")

#Método de Classe
class Exemplo:
    @classmethod
    def metodo_classe(cls):
        print("Este é um método de classe.")

#Método Estático   
class Exemplo:
    @staticmethod
    def metodo_estatico():
        print("Este é um método estático.")

#ContaBancaria.py
class ContaBancaria:
    taxa_juros = 0.05
    total_contas = 0

    def __init__(self, saldo):
        self.saldo = saldo
        ContaBancaria.total_contas += 1

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        print(f"Saldo: R${self.saldo}")

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        cls.taxa_juros = nova_taxa

    @classmethod
    def mostrar_total_contas(cls):
        print(f"Total de contas: {cls.total_contas}")

    @staticmethod
    def converter_moeda(valor, taxa):
        return valor * taxa

    @staticmethod
    def dias_no_ano():
        return 365