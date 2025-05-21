class pessoa:
    def __init__(self, nome):
        self.__nome = nome #Atributo protegido
    


class pessoa:
    def __init__(self, nome):
        self.__nome = nome #Atributo privado
    
    def get_nome(self):
        return self.__nome

p = pessoa("Giovana")
print(p.get_nome)

class contaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo #Atributo privado
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo =saldo
        else: 
            ("saldo não pode ser negativo")

conta = contaBancaria(100)
print(conta.get_saldo())

conta.set_saldo(200)
print(conta.get_saldo())


class contaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo #Atributo privado
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0:
            self.__saldo =saldo
        else: 
            print("Saldo não pode ser negativo")

conta = contaBancaria(100)
print(conta.saldo) #Acessa usando o getter: 100

conta.saldo = 200 #modifica usando o setter
print(conta.saldo) #Acessa saldo atualizado: 200