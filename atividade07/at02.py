class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, marca, ano, tipo_guidao):
        super().__init__(marca, ano)
        self.tipo_guidao = tipo_guidao

# Exemplos:
c = Carro("Ford", 2020, 4)
m = Moto("Yamaha", 2022, "esportivo")

print(c.marca, c.ano, c.portas)
print(m.marca, m.ano, m.tipo_guidao)