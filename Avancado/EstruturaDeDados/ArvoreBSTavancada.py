# Árvore AVL em Python:

class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, chave):
        if not raiz:
            return NoAVL(chave)

        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz.direita, chave)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.balanceamento(raiz)

        # Casos de desequilíbrio e rotações
        if balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)
        if balanceamento < -1:
            if chave > raiz.direita.chave:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def inserir_chave(self, chave):
        self.raiz = self.inserir(self.raiz, chave)

    def in_order_traversal(self, no):
        if no:
            self.in_order_traversal(no.esquerda)
            print(no.chave, end=" ")
            self.in_order_traversal(no.direita)

    def imprimir_arvore(self):
        print("Árvore AVL:")
        self.in_order_traversal(self.raiz)
        print()


# Exemplo de uso:
arvore_avl = ArvoreAVL()
chaves = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for chave in chaves:
    arvore_avl.inserir_chave(chave)

arvore_avl.imprimir_arvore()
