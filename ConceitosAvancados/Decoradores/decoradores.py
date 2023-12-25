""" Decoradores em Python são funções que permitem modificar o comportamento de outras funções ou métodos sem alterar seu código-fonte. Isso é amplamente usado em frameworks web como Flask e Django para adicionar funcionalidades a rotas, validar autenticação, fazer logging, cache, entre outras coisas. Vou explicar os conceitos avançados dos decoradores e fornecer exemplos para demonstrar como usá-los"""

"""
Conceitos Avançados:

Aninhamento de Funções: Os decoradores são funções aninhadas em outras funções. Isso permite que você defina um conjunto de ações que podem ser executadas antes ou após a função que está sendo decorada.

Uso de @: O operador @ é usado para aplicar um decorador a uma função. Ele é colocado acima da definição da função que será decorada.

Funções que Aceitam Funções: Decoradores aceitam funções como argumentos e retornam funções modificadas ou decoradas.

Exemplos:

Aqui estão alguns exemplos que demonstram conceitos avançados de decoradores em Python:
"""

# Um decorador simples que exibe uma mensagem antes e depois de executar a função.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finalizado {func.__name__}")
        return result
    return wrapper

@log_decorator
def somar(a, b):
    return a + b

resultado = somar(3, 5)
# Saída:
# Executando somar
# Finalizado somar

print("Resultado:", resultado)  # Saída: Resultado: 8

""" Neste exemplo, log_decorator é um decorador que envolve a função somar. Ele exibe mensagens antes e depois de executar a função. O @log_decorator é usado para aplicar o decorador à função somar."""

# Um decorador com argumentos que limita a execução da função.
def limite_de_execucoes(max_execucoes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.execucoes < max_execucoes:
                result = func(*args, **kwargs)
                wrapper.execucoes += 1
                return result
            else:
                print("Limite de execuções excedido")
        wrapper.execucoes = 0
        return wrapper
    return decorator

@limite_de_execucoes(3)
def contar():
    print("Contagem")

contar()
contar()
contar()
contar()  # Saída: Limite de execuções excedido

"""
Neste exemplo, limite_de_execucoes é um decorador que aceita um argumento max_execucoes para limitar o número de vezes que a função contar pode ser executada.

Decoradores são uma parte fundamental da programação em Python e permitem que você adicione funcionalidades reutilizáveis a funções e métodos de maneira limpa e modular. Eles são amplamente usados em frameworks web, como Flask e Django, para adicionar recursos a rotas, validações, autenticação, autorização e muito mais.
"""