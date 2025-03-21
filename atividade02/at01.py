#Exercicio 1 - Listas
# a) Criar uma lista de números e imprimir apenas os ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números ímpares:")
for num in numeros:
    if num % 2 != 0:
        print(num)

#  Removendo todos os números pares com while
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        numeros.pop(i)
    else:
        i += 1

print("Lista após remoção dos números pares:", numeros)

# b) Criar uma lista de frutas e adicionar uma nova se não estiver na lista
frutas = ["maçã", "banana", "uva"]
nova_fruta = "laranja"

if nova_fruta not in frutas:
    frutas.append(nova_fruta)

print("Lista de frutas atualizada:", frutas)
