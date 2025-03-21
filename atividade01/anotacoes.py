vetor =[]
while True:
    nome = input("Informe um nome: ")
    opecao = input("Gostaria de colocar um novo nome? S para sim e N para não ")
    vetor.append(nome)

    #Função upper para compreender independente se for maiusculo ou não
    if opecao.upper() == "S":
        print("Coloque mais um: ")
        
    else:
        #Quebra de ciclo do while
        break

    print(vetor)

#Adicionar apenas se for impares
for i in range(10):
    if i % 2 == 0:
        continue #Pula os números que não forem impares
    print(i)

#Função pass, ele é nulo, apenas passa algo
    if opecao.upper() == "S":
        pass
        
    else:
        #Quebra de ciclo do while
        break