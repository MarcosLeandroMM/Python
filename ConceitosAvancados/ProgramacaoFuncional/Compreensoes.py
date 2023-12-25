""" As compreensões de lista são uma maneira concisa de criar listas em Python usando uma única linha de código. """

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

"""
As compreensões de lista podem incluir filtros e expressões lambda:
"""
numeros = [1, 2, 3, 4, 5]
pares_quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(pares_quadrados)  # Saída: [4, 16]

