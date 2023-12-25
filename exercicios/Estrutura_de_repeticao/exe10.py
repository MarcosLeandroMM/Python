# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
'''comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math

area_em_metros = float(input("Digite o valor em metros da área a ser pintada: "))
cobertura_da_tinta = area_em_metros / 6
lata_litros = 18
valor_lata = 80
galao_litro = 3,6
galao_Valor = 25


qtd_de_tintas18 = cobertura_da_tinta / lata_litros
preco_tintas18 = qtd_de_tintas18 * valor_lata

qtd_de_galao = cobertura_da_tinta / galao_litro
preco_galao = qtd_de_galao * galao_Valor

qtd_latas_misturadas = int(qtd_de_tintas18 / lata_litros)
resto_tinta = qtd_de_tintas18 % lata_litros
qtd_galoes_misturados = math.ceil(resto_tinta / lata_litros)

# Calcula o preço total com mistura de latas e galões
preco_total_misturado = (qtd_latas_misturadas * valor_lata) + (qtd_galoes_misturados * preco_galao)

# Exibe os resultados
print(f"Quantidade de latas de 18 litros: {qtd_de_tintas18}")
print(f"Preço total com latas de 18 litros: R$ {preco_tintas18:.2f}")

print(f"Quantidade de galões de 3,6 litros: {qtd_de_galao}")
print(f"Preço total com galões de 3,6 litros: R$ {preco_galao:.2f}")

print(f"Quantidade de latas de 18 litros e galões de 3,6 litros misturados:")
print(f"Latas: {qtd_latas_misturadas}")
print(f"Galões: {qtd_galoes_misturados}")
print(f"Preço total com mistura de latas e galões: R$ {preco_total_misturado:.2f}")

