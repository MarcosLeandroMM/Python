# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metroArea = float(input("Digite o valor em metros da área: "))
coberturaDaTinta = metroArea / 3
lata = 18
valorTinta = 80

qtdDeLatas = coberturaDaTinta / lata
precoTotal = qtdDeLatas * valorTinta

print(f"A quantidade de latas necessárias para esta quantidade de metro fornecida é de {qtdDeLatas:.2f} ficando no valor de {precoTotal:.2f}")