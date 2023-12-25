"""
Metaclasses e design patterns são conceitos avançados em Python que permitem uma flexibilidade e personalização significativamente maiores na construção de classes e objetos. Vou explicar brevemente esses conceitos e fornecer exemplos de como eles podem ser usados juntos.

Metaclasses:

As metaclasses são classes de classes. Em Python, todas as classes são instâncias de metaclasses, com a metaclasses padrão sendo geralmente a classe type. Você pode criar suas próprias metaclasses para personalizar o comportamento das classes. As metaclasses são muitas vezes usadas para aplicar lógica global em classes ou para impor regras de construção.

Design Patterns:

Design patterns são soluções comprovadas para problemas comuns de design de software. Eles são maneiras de organizar o código de forma que seja mais eficiente, fácil de entender e manter. Em Python, os design patterns podem ser implementados usando metaclasses, pois permitem uma abordagem mais flexível e orientada a objetos para a construção de classes.

Exemplo de Metaclasses e Design Patterns:

Aqui está um exemplo de como as metaclasses e design patterns podem ser usados juntos. Vamos criar um Singleton, um padrão de design que garante que uma classe tenha apenas uma instância durante toda a vida do programa:
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Testando o Singleton
singleton_1 = Singleton(1)
singleton_2 = Singleton(2)

print(singleton_1.value)  # Saída: 1
print(singleton_2.value)  # Saída: 1 (mesma instância)

print(singleton_1 is singleton_2)  # Saída: True (são a mesma instância)

"""
Neste exemplo, SingletonMeta é uma metaclass que garante que a classe Singleton tenha apenas uma instância, criando um dicionário _instances que mantém o controle de instâncias já criadas.

Em seguida, a classe Singleton é definida com um construtor que aceita um valor. Graças à metaclass, a classe Singleton agora é um Singleton, o que significa que qualquer tentativa de criar uma nova instância resultará na recuperação da instância existente.

Essa é apenas uma demonstração simples de como metaclasses e design patterns podem ser combinados em Python. O uso de metaclasses pode ser muito poderoso quando se trata de personalizar a construção de classes e aplicar padrões de design de maneira elegante.
"""

"""
O uso de * e ** nos argumentos de uma função em Python permite que você lide com argumentos variáveis e parâmetros de palavra-chave de maneira flexível. Aqui estão os conceitos e exemplos relacionados a * e **:

* (Asterisco):

*args é usado para coletar argumentos posicionais variáveis em uma tupla.
Permite que você passe um número arbitrário de argumentos posicionais para a função.
Os argumentos são empacotados em uma tupla.
"""
def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = somar(1, 2, 3, 4, 5)
print(resultado)  # Saída: 15

"""
** (Dois asteriscos):

**kwargs é usado para coletar argumentos de palavra-chave variáveis em um dicionário.
Permite que você passe um número arbitrário de argumentos de palavra-chave para a função.
Os argumentos de palavra-chave são empacotados em um dicionário.
"""

def criar_dicionario(**kwargs):
    return kwargs

dicionario = criar_dicionario(nome="Alice", idade=30, cidade="Nova York")
print(dicionario)  # Saída: {'nome': 'Alice', 'idade': 30, 'cidade': 'Nova York'}

"""
Uso combinado de * e **:

Você pode usar * e ** juntos em uma função para aceitar argumentos posicionais e de palavra-chave variáveis.
"""

def exemplo_combinado(arg1, arg2, *args, kwarg1=0, **kwargs):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("args:", args)
    print("kwarg1:", kwarg1)
    print("kwargs:", kwargs)

exemplo_combinado(1, 2, 3, 4, kwarg1=5, nome="Alice", idade=30)

""" Neste exemplo, arg1 e arg2 são argumentos posicionais fixos, args é uma tupla que coleta argumentos posicionais adicionais, kwarg1 é um argumento de palavra-chave fixo, e kwargs é um dicionário que coleta argumentos de palavra-chave adicionais.

O uso de *args e **kwargs é útil quando você deseja criar funções flexíveis que podem lidar com diferentes números de argumentos posicionais e de palavra-chave sem a necessidade de especificar todos eles antecipadamente. Isso é especialmente útil em casos onde a quantidade de argumentos é desconhecida ou pode variar."""