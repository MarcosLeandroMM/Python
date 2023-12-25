'''
Ordenação Personalizada:
Crie uma função de ordenação personalizada que aceita uma lista de strings e as classifica com base na quantidade de vogais em cada string.

'''

def contar_vogais(string):
    vogais = "AEIOUaeiou"
    return sum(1 for char in string if char in vogais)

def ordenar_por_vogais(lista_de_strings):
    return sorted(lista_de_strings, key=contar_vogais)

# Exemplo de uso:
strings = ["banana", "abracadabra", "hello", "python", "programming"]

lista_ordenada = ordenar_por_vogais(strings)

for string in lista_ordenada:
    print(string)
