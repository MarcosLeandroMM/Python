'''
Recursão Avançada:
Implemente uma função recursiva que calcule o fatorial de um número, mas use recursão de cauda para evitar o estouro de pilha.

'''

def factorial_tail_recursive(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n - 1, n * accumulator)

# Exemplo de uso:
n = 5  # Substitua pelo número para o qual você deseja calcular o fatorial
result = factorial_tail_recursive(n)
print(f'{n}! = {result}')

'''
Nesta implementação, a função factorial_tail_recursive aceita dois argumentos: n (o número para o qual você deseja calcular o fatorial) e accumulator (o valor acumulado até o momento). A função realiza a recursão de cauda, onde o resultado é acumulado multiplicando n pelo accumulator, e n é decrementado em cada chamada recursiva. A recursão continua até que n seja igual a 0, momento em que o acumulador contém o fatorial calculado.

Isso evita o estouro de pilha que ocorre na recursão tradicional e permite calcular fatoriais de números maiores de forma eficiente.
'''

'''

Estouro de Pilha (Stack Overflow):

O estouro de pilha ocorre quando uma função recursiva faz chamadas recursivas demais antes de chegar a um caso base, levando ao esgotamento da pilha de chamadas.
Em linguagens de programação, como Python, C++, Java, e muitas outras, a pilha de chamadas (stack) é usada para rastrear as chamadas de funções e suas variáveis locais.
Cada vez que uma função é chamada, informações sobre a chamada, como os parâmetros e variáveis locais, são empilhadas na pilha de chamadas.
Quando uma função recursiva é chamada, a pilha de chamadas cresce, e quando a recursão é concluída, a pilha é desempilhada. Se a recursão não atingir o caso base, a pilha de chamadas pode ficar sem espaço, resultando em um erro de estouro de pilha.
Recursão de Cauda (Tail Recursion):

A recursão de cauda é um tipo especial de recursão em que a chamada recursiva é a última operação executada em uma função.
Em outras palavras, na recursão de cauda, o resultado da chamada recursiva é diretamente retornado como o resultado da função atual.
Isso permite que algumas linguagens de programação otimizem automaticamente a recursão de cauda, evitando o estouro de pilha, pois a pilha de chamadas pode ser reutilizada para cada chamada recursiva.
As linguagens de programação que suportam otimização de recursão de cauda podem calcular fatoriais e executar outras funções recursivas de forma eficiente, mesmo para entradas grandes, sem causar estouro de pilha.
Nem todas as linguagens de programação oferecem otimização de recursão de cauda, mas aquelas que o fazem, como algumas implementações de Python, podem permitir que você escreva funções recursivas de forma mais segura em termos de uso de memória. Caso contrário, é necessário usar abordagens iterativas ou outras técnicas para evitar estouros de pilha em funções recursivas.

'''