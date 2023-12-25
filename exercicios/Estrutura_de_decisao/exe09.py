# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Classifica a lista em ordem decrescente
numeros_decrescente = sorted(numeros, reverse=True)

# Exibe os números em ordem decrescente
print("Números em ordem decrescente:")
for numero in numeros_decrescente:
    print(numero)