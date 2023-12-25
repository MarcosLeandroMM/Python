'''
Map, Filter e Reduce:
Escreva funções personalizadas chamadas meu_map, meu_filter e meu_reduce que imitam o comportamento das funções embutidas map, filter e reduce.
'''

from functools import reduce  # Importar reduce da biblioteca functools para a implementação de meu_reduce

# Implementação de meu_map
def meu_map(funcao, iteravel):
    resultado = []
    for item in iteravel:
        resultado.append(funcao(item))
    return resultado

# Implementação de meu_filter
def meu_filter(funcao, iteravel):
    resultado = []
    for item in iteravel:
        if funcao(item):
            resultado.append(item)
    return resultado

# Implementação de meu_reduce
def meu_reduce(funcao, iteravel, valor_inicial=None):
    iteravel = iter(iteravel)
    
    if valor_inicial is None:
        valor_acumulado = next(iteravel)
    else:
        valor_acumulado = valor_inicial
    
    for item in iteravel:
        valor_acumulado = funcao(valor_acumulado, item)
    
    return valor_acumulado

# Exemplos de uso:
# Função para elevar ao quadrado
def quadrado(x):
    return x ** 2

# Função para filtrar números pares
def numeros_pares(x):
    return x % 2 == 0

# Função para somar
def soma(x, y):
    return x + y

lista = [1, 2, 3, 4, 5]

# Usando meu_map para calcular o quadrado de cada elemento da lista
resultado_map = meu_map(quadrado, lista)
print("meu_map:", resultado_map)

# Usando meu_filter para filtrar os números pares
resultado_filter = meu_filter(numeros_pares, lista)
print("meu_filter:", resultado_filter)

# Usando meu_reduce para somar todos os elementos da lista
resultado_reduce = meu_reduce(soma, lista)
print("meu_reduce:", resultado_reduce)

'''
Nas implementações acima, meu_map aplica a função funcao a cada item no iterável, meu_filter filtra os itens com base na função funcao e meu_reduce reduz a lista a um único valor usando a função funcao. Certifique-se de adaptar as funções e iteráveis conforme necessário para suas próprias necessidades.

'''