#Exercicio 1 break com while
#while True:
 #   num = input("Digite um número (0 para sair): ")

  #  if num == 0:
   #     print("Programa encerrado")
    #    break

#Exercicio 2 continue num loop for
for i in range (1, 11):
    if i % 3 == 0:
        continue
    print(i)

#Exercicio 3 pass em condicional 
num = input("Digite um número: ")

for num in range(10):
 if num % 2 == 0:
    continue #Pula os números que não forem impares
    print(num)
