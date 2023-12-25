# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

vetor = []

for i in range(5):
    idade = int(input(f"Digite a {i+1}° idade: "))
    vetor.append(idade)
    
