'''
Fibonacci Recursivo com Memoização:
Implemente uma função que calcule o n-ésimo termo da sequência de Fibonacci usando recursão e memoização para evitar cálculos repetidos.



'''

def fibonacci_recursive_memoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        result = n
    else:
        result = fibonacci_recursive_memoization(n - 1, memo) + fibonacci_recursive_memoization(n - 2, memo)

    memo[n] = result
    return result

# Exemplo de uso:
n = 10  # Substitua pelo valor de n que você deseja calcular
result = fibonacci_recursive_memoization(n)
print(f'O {n}-ésimo termo da sequência de Fibonacci é: {result}')

'''
Nesta implementação, usamos um dicionário chamado memo para armazenar os valores já calculados. Quando a função fibonacci_recursive_memoization é chamada para um valor de n, ela verifica se o valor já foi calculado e armazenado no dicionário memo. Se sim, ela retorna o valor armazenado em vez de recalculá-lo. Isso melhora significativamente o desempenho, especialmente para valores maiores de n.

'''

'''
Recursão é uma técnica de programação em que uma função chama a si mesma repetidamente até que uma condição de término seja satisfeita. Alguns dos exemplos onde a recursão é usada são: cálculo da série de fibonacci , fatorial etc. Mas o problema com eles é que na árvore de recursão, pode haver chances de que o subproblema já resolvido esteja sendo resolvido novamente, o que adiciona para uma sobrecarga.

Memoização é uma técnica de registro de resultados intermediários para que possa ser utilizada para evitar cálculos repetidos e agilizar os programas. Pode ser usado para otimizar os programas que usam recursão. Em Python, a memoização pode ser feita com a ajuda de decoradores de função.
'''