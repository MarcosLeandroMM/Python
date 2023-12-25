# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O primeiro produto é o mais barato e deve ser comprado!")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O segundo produto é o mais barato e deve ser comprado!")
else:
    print("O terceiro produto é o mais barato e deve ser comprado!")