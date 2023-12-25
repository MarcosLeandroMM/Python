"""Funções de Ordem Superior:

Funções de ordem superior são funções que tratam outras funções como argumentos ou retornam funções como resultados. Elas são uma parte fundamental da programação funcional em Python.

Exemplo de Função de Ordem Superior: map
map: A função map aplica uma função a cada elemento de um iterável e retorna um novo iterável com os resultados.
"""

def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
resultado = map(dobrar, numeros)
# Convertendo o resultado para uma lista
lista_resultado = list(resultado)
print(lista_resultado)  # Saída: [2, 4, 6, 8, 10]


"""
reduce: A função reduce aplica uma função cumulativamente a elementos de um iterável, reduzindo-os a um único valor.

Para usar reduce, você precisa importá-lo do módulo functools.

Exemplo:
"""

from functools import reduce

def somar(x, y):
    return x + y

numeros = [1, 2, 3, 4, 5]
resultado = reduce(somar, numeros)
print(resultado)  # Saída: 15 (1 + 2 + 3 + 4 + 5)


"""filter: A função filter filtra elementos de um iterável com base em uma função de teste.

Exemplo: 
"""

def par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filter(par, numeros)
# Convertendo o resultado para uma lista
lista_resultado = list(resultado)
print(lista_resultado)  # Saída: [2, 4, 6, 8, 10]
