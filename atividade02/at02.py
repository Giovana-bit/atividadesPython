#Exercício 2 - Tupla
# a) Converter temperaturas de Celsius para Fahrenheit
tempC = (0, 25, 30, 40)
tempF= tuple((c * 9/5) + 32 for c in tempC)

print("Temperaturas em Fahrenheit:", tempF)

# b) Criar uma tupla de coordenadas e verificar se x é maior que 0
coordenadas = (3, -2) 
x, y = coordenadas

if x > 0:
    print("A coordenada x é maior que 0.")
else:
    print("A coordenada x não é maior que 0.")