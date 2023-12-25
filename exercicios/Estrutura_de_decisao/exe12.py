'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

'''
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

salario_bruto = horas_trabalhadas * valor_hora
salario_funcionario = salario_bruto

if salario_funcionario <= 900:
    valor_ir = 0
    desconto_ir = 0
elif salario_funcionario <= 1500:
    valor_ir = 0.05
    desconto_ir = salario_funcionario * valor_ir
elif salario_funcionario <= 2500:
    valor_ir = 0.1
    desconto_ir = salario_funcionario * valor_ir
else:
    valor_ir = 0.2
    desconto_ir = salario_funcionario * valor_ir

desconto_sindicato = salario_funcionario * 0.03
valor_fgts = 0.11 * salario_funcionario
desconto_total = desconto_ir + desconto_sindicato

salario_liquido = salario_funcionario - desconto_total

# Imprimir as informações
print("\nFolha de Pagamento")
print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR ({valor_ir * 100}%): R$ {desconto_ir:.2f}")
print(f"(-) Sindicato (3%): R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%): R$ {valor_fgts:.2f}")
print(f"Total de descontos: R$ {desconto_total:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")