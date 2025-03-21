# Exercicio 1 - Calculo da Idade

#adicionando input para o usuario
anoNascimento = int(input("Coloque seu ano de nascimento: "))

anoAtual = 2025
idade = anoAtual - anoNascimento

print(f"Sua idade é: {idade} anos")

#Exercicio 2 - altura ao Quadrado

#adicionando input para o usuario
altura = float(input("Coloque sua altura em metros(M): "))

alturaQuadrado = altura ** 2

print(f"Sua altura ao quadrado: {alturaQuadrado} Metros quadrados")

#Exercicio 3 - Verificação para maior de idade

#usando o mesmo input do primeiro exercicio!
maiorIdade = idade >= 18

print (f"É maior de idade {maiorIdade}")

#Exercicio 4 - Verificar quem é mais alto

alturaProf = 1.67
maisAlto = altura > alturaProf

print (f"É mais alto que 1.67m {maisAlto}")

#Exercicio 5 - combinando condições

requisitos = maiorIdade and maisAlto

print (f"Atende requisitos de ser maior de idade e mais alto que 1.67? {requisitos}")
