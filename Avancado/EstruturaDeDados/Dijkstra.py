
"""
 O algoritmo de Dijkstra é um exemplo clássico de seleção baseada em prioridade para encontrar o caminho mais curto em um grafo ponderado. Vou fornecer um exemplo prático de implementação do algoritmo de Dijkstra em Python usando uma fila de prioridade com heap.

python
"""

import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        self.distancias = {}

    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        self.arestas[vertice] = []

    def adicionar_aresta(self, origem, destino, peso):
        self.arestas[origem].append((destino, peso))
        self.arestas[destino].append((origem, peso))

    def dijkstra(self, origem):
        fila_prioridade = [(0, origem)]  # (distância, vértice)
        heapq.heapify(fila_prioridade)
        self.distancias[origem] = 0

        while fila_prioridade:
            atual_distancia, atual_vertice = heapq.heappop(fila_prioridade)

            if atual_distancia > self.distancias[atual_vertice]:
                continue  # Ignorar se já encontramos um caminho mais curto

            for vizinho, peso in self.arestas[atual_vertice]:
                distancia = atual_distancia + peso

                if distancia < self.distancias.get(vizinho, float('inf')):
                    self.distancias[vizinho] = distancia
                    heapq.heappush(fila_prioridade, (distancia, vizinho))

# Exemplo de uso:
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')

grafo.adicionar_aresta('A', 'B', 1)
grafo.adicionar_aresta('A', 'C', 4)
grafo.adicionar_aresta('B', 'C', 2)
grafo.adicionar_aresta('B', 'D', 5)
grafo.adicionar_aresta('C', 'D', 1)

origem = 'A'
grafo.dijkstra(origem)

print(f"Distâncias mínimas a partir de {origem}: {grafo.distancias}")


"""
Neste exemplo, a classe Grafo representa um grafo ponderado não direcionado. O método dijkstra implementa o algoritmo de Dijkstra usando uma fila de prioridade com heap. O resultado é um dicionário distancias que contém as distâncias mínimas de origem para todos os outros vértices no grafo.
"""