'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

'''
# Imprime os números de 1 a 20 um abaixo do outro
numero = 1
while numero <= 20:
    print(numero)
    numero += 1

# Imprime os números de 1 a 20 um ao lado do outro
numero = 1
while numero <= 20:
    print(numero, end=" ")  # O parâmetro end=" " adiciona um espaço em vez de uma quebra de linha
    numero += 1