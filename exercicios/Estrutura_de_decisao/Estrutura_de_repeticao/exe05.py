'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

'''

pais_A = float(input("Digite a população do país A: "))


Pais_B = float(input("Digite a taxa de crescimento do país B: "))

taxa_de_crescimento_A = 0.03
taxa_de_crescimento_B = 0.015
anos = 0

while pais_A < Pais_B:
    pais_A += pais_A * taxa_de_crescimento_A
    Pais_B += Pais_B * taxa_de_crescimento_B
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar a população do país B.")


