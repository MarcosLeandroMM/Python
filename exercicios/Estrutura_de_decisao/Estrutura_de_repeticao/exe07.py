'''
Faça um programa que leia 5 números e informe o maior número

'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))
num3 = int(input("Digite um terceiro número: "))
num4 = int(input("Digite um quarto número: "))
num5 = int(input("Digite um quinto número: "))

maiorNumero = max(num1, num2, num3, num4, num5)

print(f"O maior número entre os 5 cincos números é {maiorNumero}")