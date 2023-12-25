
'''Fila de Prioridade com Heap:
Escreva uma implementação de uma fila de prioridade usando uma estrutura de heap (árvore binária). Implemente operações de inserção e remoção, garantindo que o elemento de maior prioridade seja sempre o primeiro da fila.
'''

import heapq

class FilaPrioridadeHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, elemento, prioridade):
        heapq.heappush(self.heap, (prioridade, elemento))

    def remover(self):
        if self.esta_vazia():
            raise IndexError("A fila de prioridade está vazia")
        _, elemento = heapq.heappop(self.heap)
        return elemento

    def esta_vazia(self):
        return len(self.heap) == 0

# Exemplo de uso:
fila_prioridade = FilaPrioridadeHeap()

# Inserir elementos com prioridades
fila_prioridade.inserir('Tarefa 1', 3)
fila_prioridade.inserir('Tarefa 2', 1)
fila_prioridade.inserir('Tarefa 3', 2)

# Remover elementos de acordo com a prioridade
while not fila_prioridade.esta_vazia():
    print(fila_prioridade.remover())

"""
Neste exemplo, a fila de prioridade é implementada usando a função heappush para inserir elementos e heappop para remover o elemento de menor prioridade. A função heappop garante que o elemento removido seja sempre o de menor prioridade na heap.

Esta implementação é eficiente e é amplamente utilizada em algoritmos que envolvem seleção baseada em prioridade, como o algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo ponderado.

"""