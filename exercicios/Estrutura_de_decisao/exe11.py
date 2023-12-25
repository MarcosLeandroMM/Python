salario_funcionario = float(input("Digite o valor do salário: "))

# Defina os percentuais de aumento em um dicionário
percentuais_aumento = {
    1: 0.2,  # Salário até R$ 280
    2: 0.15,  # Salário entre R$ 280 e R$ 700
    3: 0.1,  # Salário entre R$ 700 e R$ 1500
    4: 0.05  # Salário acima de R$ 1500
}

# Encontre o intervalo correspondente com base no salário
if salario_funcionario <= 280:
    intervalo = 1
elif salario_funcionario <= 700:
    intervalo = 2
elif salario_funcionario <= 1500:
    intervalo = 3
else:
    intervalo = 4

# Calcule o aumento e o novo salário
percentual_de_aumento = percentuais_aumento[intervalo]
valor_do_aumento = salario_funcionario * percentual_de_aumento
salario_reajustado = salario_funcionario + valor_do_aumento

# Imprima os resultados
print(f"Salário antes do reajuste: R$ {salario_funcionario:.2f}")
print(f"Percentual de aumento: {percentual_de_aumento * 100}%")
print(f"Valor do aumento: R$ {valor_do_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {salario_reajustado:.2f}")