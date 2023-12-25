# criando uma função que escreve a série de Fibonnacci até um limite arbitrário

def fib(n):
    """Print a Fibonacci series up to on."""
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()

f = fib
f(100)

# função que retorna uma lista de números da série de Fibonacci

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)
