'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

'''
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarValorLado(self, novo_largura):
        self.largura = novo_largura

    def retornarValorLado(self):
        return self.largura  # Corrigido para retornar o valor atual da largura

    def calcularArea(self):
        return self.comprimento * self.largura  # Corrigido para calcular a área corretamente

    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)  # Corrigido para calcular o perímetro corretamente

# Criando um objeto retângulo
retangulo = Retangulo(20, 40)

# Mudando o valor da largura
retangulo.mudarValorLado(10)

# Retornando o valor atual da largura
retornar_valor_lado = retangulo.retornarValorLado()

# Calculando a área
calc_area = retangulo.calcularArea()

# Calculando o perímetro
calc_peri = retangulo.calcularPerimetro()

print("O lado do retângulo é:", retornar_valor_lado)
print("A área do retângulo é:", calc_area)
print("O perímetro do Retângulo é:", calc_peri)


