'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;''' 


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudarValorDoLado(self, novo_valor_lado):
        self.tamanho_do_lado = novo_valor_lado

    def retornarValorDoLado(self):
        return self.tamanho_do_lado

    def calcularArea(self):
        return self.tamanho_do_lado ** 2

# Criar um objeto Quadrado
quadrado = Quadrado(10)

# Trocar o valor do lado
quadrado.mudarValorDoLado(20)

# Obter o novo valor do lado
novo_valor_lado = quadrado.retornarValorDoLado()

# Calcular a área do quadrado
area = quadrado.calcularArea()

print("O novo valor do lado é", novo_valor_lado)
print("A área do quadrado é", area)    