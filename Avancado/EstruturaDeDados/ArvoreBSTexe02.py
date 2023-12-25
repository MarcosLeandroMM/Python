'''

Árvore Binária de Busca:
Escreva uma classe que represente uma árvore binária de busca e implemente operações de inserção, remoção e busca.

'''

# Árvore Binária de Busca (BST - Binary Search Tree) com operações de inserção, remoção e busca:

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if not no:
            return No(chave)

        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._inserir_recursivo(no.direita, chave)

        return no

    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, no, chave):
        if not no:
            return no

        if chave < no.chave:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda

            no.chave = self._min_valor(no.direita)
            no.direita = self._remover_recursivo(no.direita, no.chave)

        return no

    def _min_valor(self, no):
        while no.esquerda:
            no = no.esquerda
        return no.chave

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if not no or no.chave == chave:
            return no

        if chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)


# Exemplo de uso:
arvore = ArvoreBinariaBusca()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print("Árvore original:")
# Saída esperada: 20 30 40 50 60 70 80
# Representa a travessia em ordem (in-order) da árvore
def in_order_traversal(node):
    if node:
        in_order_traversal(node.esquerda)
        print(node.chave, end=" ")
        in_order_traversal(node.direita)

in_order_traversal(arvore.raiz)
print()

arvore.remover(30)
print("Árvore após a remoção do nó com chave 30:")
# Saída esperada: 20 40 50 60 70 80
in_order_traversal(arvore.raiz)
print()

# Testar busca
chave = 60
resultado_busca = arvore.buscar(chave)
if resultado_busca:
    print(f"Chave {chave} encontrada na árvore.")
else:
    print(f"Chave {chave} não encontrada na árvore.")


"""
Neste exemplo, a classe ArvoreAVL possui métodos adicionais para realizar rotações e verificar o balanceamento dos nós. Isso ajuda a manter a árvore balanceada após operações de inserção. Este é apenas um exemplo, e existem outras árvores de busca balanceadas, como a Árvore Rubro-Negra, que também podem ser implementadas para atender a diferentes requisitos de desempenho.

"""