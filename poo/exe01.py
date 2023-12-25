'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor 
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor
    

# criando objeto Bola
minha_bola = Bola("vermelha", 30, "couro")

# mostrar a cor da bola
print("Cor da bola:", minha_bola.mostraCor())

# trocar a cor da bola
minha_bola.trocaCor("azul")

# mostrar a nova cor da bola
print("Nova cor da bola:", minha_bola.mostraCor())
    
        