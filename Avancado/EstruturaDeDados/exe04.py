'''
Tabela de Hash Personalizada:
Implemente uma tabela de hash personalizada que permita inserir, buscar e remover elementos, lidando com colisões por meio de listas encadeadas.

'''

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        if self.tabela[indice] is None:
            self.tabela[indice] = No(chave, valor)
        else:
            atual = self.tabela[indice]
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = No(chave, valor)

    def buscar(self, chave):
        indice = self._hash(chave)
        atual = self.tabela[indice]
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        raise KeyError(f'Chave {chave} não encontrada.')

    def remover(self, chave):
        indice = self._hash(chave)
        atual = self.tabela[indice]
        anterior = None

        while atual:
            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[indice] = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        raise KeyError(f'Chave {chave} não encontrada.')

# Exemplo de uso:
tabela_hash = TabelaHash()

# Inserir elementos
tabela_hash.inserir('a', 1)
tabela_hash.inserir('b', 2)
tabela_hash.inserir('c', 3)

# Buscar elementos
print(tabela_hash.buscar('a'))  # Saída esperada: 1
print(tabela_hash.buscar('b'))  # Saída esperada: 2

# Remover elemento
tabela_hash.remover('b')
try:
    print(tabela_hash.buscar('b'))
except KeyError as e:
    print(e)  # Saída esperada: Chave 'b' não encontrada.

"""
Nesta implementação, a função de hash _hash determina o índice na tabela para cada chave. Se houver uma colisão, isto é, se dois elementos tiverem o mesmo índice, uma lista encadeada é usada para armazenar esses elementos. A classe No representa os elementos da lista encadeada. A tabela é inicializada com uma lista de None, e a inserção, busca e remoção são implementadas de acordo.

"""