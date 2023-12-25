# Básico - Tabuada: Crie um programa que peça ao usuário para digitar um número e, em seguida, imprima a tabuada desse número de 1 a 10.

# Solicita ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Calcula e imprime a tabuada do número de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")