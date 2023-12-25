'''
Funções de Ordem Superior:
Crie uma função de ordem superior chamada aplicar_funcao que aceita uma função e uma lista de números como argumentos e aplica a função a cada número na lista, retornando uma lista com os resultados.
'''

def aplicar_funcao(funcao, numeros):
    resultados = []
    for numero in numeros:
        resultado = funcao(numero)
        resultados.append(resultado)
    return resultados

# Exemplos de funções que podem ser usadas com a aplicar_funcao:
def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar a função quadrado a cada número na lista
resultados_quadrado = aplicar_funcao(quadrado, numeros)
print("Resultados com a função quadrado:", resultados_quadrado)

# Aplicar a função cubo a cada número na lista
resultados_cubo = aplicar_funcao(cubo, numeros)
print("Resultados com a função cubo:", resultados_cubo)
