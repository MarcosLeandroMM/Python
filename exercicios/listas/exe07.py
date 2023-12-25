# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# Crie uma lista vazia para armazenar os números
vetor = []

# Use um loop para ler os 5 números do usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Calcule a soma e a multiplicação dos números
soma = sum(vetor)

# Você também pode calcular a multiplicação usando um loop
multiplicacao = 1
for numero in vetor:
    multiplicacao *= numero

# Imprima os números, soma e multiplicação
print(f"Números digitados: {vetor}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação dos números: {multiplicacao}")
