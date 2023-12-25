# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input("Quanto você ganha por hora: "))
horasTrabalhadas = float(input("Número de horas trabalhadas: "))

salario = valorPorHora * horasTrabalhadas

print(f"O salário no mês é {salario}")
