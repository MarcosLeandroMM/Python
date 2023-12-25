'''

Implementação de um Grafo Direcionado:
Crie uma classe que represente um grafo direcionado e implemente algoritmos de busca em profundidade (DFS) e busca em largura (BFS) para percorrer o grafo.

'''

# Aqui está uma implementação básica de um grafo direcionado em Python, com os algoritmos de busca em profundidade (DFS) e busca em largura (BFS):

from collections import defaultdict, deque

class GrafoDirecionado:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, origem, destino):
        self.grafo[origem].append(destino)

    def dfs(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(vertice)
        print(vertice, end=' ')

        for vizinho in self.grafo[vertice]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def bfs(self, vertice):
        visitados = set()
        fila = deque([vertice])

        while fila:
            vertice_atual = fila.popleft()
            if vertice_atual not in visitados:
                print(vertice_atual, end=' ')
                visitados.add(vertice_atual)
                fila.extend(vizinho for vizinho in self.grafo[vertice_atual] if vizinho not in visitados)

# Exemplo de uso:
grafo = GrafoDirecionado()
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 0)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 3)

print("Busca em Profundidade (DFS):")
grafo.dfs(2)
print("\n")

print("Busca em Largura (BFS):")
grafo.bfs(2)

"""
Neste exemplo, a classe GrafoDirecionado tem métodos para adicionar arestas, realizar busca em profundidade (DFS) e busca em largura (BFS). A representação do grafo é feita usando um dicionário padrão do Python, onde as chaves são os vértices e os valores são listas de vértices adjacentes.

O método dfs (busca em profundidade) utiliza uma abordagem recursiva, enquanto o método bfs (busca em largura) utiliza uma fila para percorrer os vértices em largura a partir do vértice inicial.
"""