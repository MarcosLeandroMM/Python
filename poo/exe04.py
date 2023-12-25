'''
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

'''

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return 2 * (self.comprimento + self.largura)

# Solicitar as medidas do local ao usuário
comprimento_local = float(input("Informe o comprimento do local (em metros): "))
largura_local = float(input("Informe a largura do local (em metros): "))

# Criar um objeto retângulo com as medidas do local
local = Retangulo(comprimento_local, largura_local)

# Solicitar as medidas do piso e do rodapé ao usuário
comprimento_piso = float(input("Informe o comprimento do piso (em metros): "))
largura_piso = float(input("Informe a largura do piso (em metros): "))
comprimento_rodape = float(input("Informe o comprimento do rodapé (em metros): "))

# Calcular a área do piso
area_piso = comprimento_piso * largura_piso

# Calcular a área do rodapé
area_rodape = comprimento_rodape * largura_piso  # Supondo que o rodapé tenha a mesma largura do piso

# Calcular a quantidade de pisos necessários
quantidade_pisos = local.calcularArea() / area_piso

# Calcular a quantidade de rodapés necessários
quantidade_rodapes = local.calcularPerimetro() / comprimento_rodape

# Arredondar para cima para garantir que você tenha o suficiente
import math
quantidade_pisos = math.ceil(quantidade_pisos)
quantidade_rodapes = math.ceil(quantidade_rodapes)

# Exibir os resultados
print(f"Quantidade de pisos necessários: {quantidade_pisos}")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")
