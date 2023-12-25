"""
O gerenciamento de memória é um aspecto fundamental da programação em Python, pois a linguagem utiliza um coletor de lixo automático para liberar memória não utilizada. Aqui estão alguns conceitos importantes e exemplos relacionados ao gerenciamento de memória em Python:

1. Alocação de Memória:

Quando você cria objetos em Python, a linguagem aloca automaticamente memória para esses objetos. É importante entender que objetos são criados dinamicamente e a memória é alocada de acordo com as necessidades do programa.

Exemplo:
"""

x = 42  # Cria um objeto inteiro e aloca memória para ele
nome = "Alice"  # Cria um objeto string e aloca memória para ele

"""
 Coleta de Lixo:

Python possui um coletor de lixo automático que monitora os objetos em uso e libera a memória de objetos que não são mais referenciados. Isso ajuda a evitar vazamentos de memória.

Exemplo:
"""

def criar_objeto():
    objeto = "Algum dado"
    return objeto  # O objeto é referenciado dentro da função

referencia = criar_objeto()  # O objeto é referenciado fora da função
# No final deste escopo, o objeto não é mais referenciado e pode ser coletado pelo coletor de lixo

"""
Uso Eficiente de Recursos:

É importante gerenciar recursos, como fechar arquivos ou conexões de banco de dados quando não são mais necessários. Isso ajuda a liberar recursos além da memória.

Exemplo:
"""

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
# O arquivo é automaticamente fechado quando sai do bloco `with`

"""
Gerenciamento de Ciclos de Vida de Objetos:

Entender o ciclo de vida dos objetos é fundamental. Você pode usar funções especiais, como __init__, __del__, __enter__, e __exit__, para gerenciar o ciclo de vida dos objetos.

Exemplo de uso de __init__ e __del__:
"""

class MinhaClasse:
    def __init__(self):
        print("Objeto criado")

    def __del__(self):
        print("Objeto destruído")

objeto = MinhaClasse()  # Saída: Objeto criado
del objeto  # Saída: Objeto destruído


"""Utilização de Ferramentas de Análise de Memória:

Você pode usar ferramentas como sys.getsizeof, gc.get_stats, tracemalloc, e outros para analisar o uso de memória em seu programa.

Exemplo de sys.getsizeo:
"""

import sys

x = [1, 2, 3, 4, 5]
tamanho = sys.getsizeof(x)  # Tamanho em bytes


