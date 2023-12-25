

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def esta_vazia(self):
        return self.primeiro is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def buscar(self, dado):
        atual = self.primeiro
        while atual is not None:
            if atual.dado == dado:
                return True
            atual = atual.proximo
        return False

    def remover(self, dado):
        if self.primeiro is None:
            return

        if self.primeiro.dado == dado:
            self.primeiro = self.primeiro.proximo
            return

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.dado == dado:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo

    def imprimir(self):
        elementos = []
        atual = self.primeiro
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo
        print(" -> ".join(map(str, elementos)))

# Exemplo de uso:
lista = ListaEncadeada()
print("A lista está vazia:", lista.esta_vazia())

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.inserir(40)

print("A lista está vazia:", lista.esta_vazia())

lista.imprimir()

print("Busca 20:", lista.buscar(20))
print("Busca 50:", lista.buscar(50))

lista.remover(20)
lista.remover(40)

lista.imprimir()
