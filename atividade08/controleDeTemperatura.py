class ControleTemperatura:
    def __init__(self):
        self.__temperatura = 0  # atributo privado

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if -50 <= valor <= 100:
            self.__temperatura = valor
        else:
            print("Temperatura inválida! Deve estar entre -50 e 100 graus Celsius.")

    def converter_para_fahrenheit(self):
        return self.__temperatura * 1.8 + 32

# Criando uma instância da classe
controle = ControleTemperatura()

# Definindo uma temperatura válida
controle.temperatura = 25
print("Temperatura em Celsius:", controle.temperatura)

# Definindo uma temperatura inválida
controle.temperatura = 150  # deve exibir mensagem de erro

# Convertendo para Fahrenheit
fahrenheit = controle.converter_para_fahrenheit()
print("Temperatura em Fahrenheit:", fahrenheit)
