'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a pessoa envelhece e tem menos de 21 anos, ela cresce 0,5 cm
            self.crescer(0.5)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

# Criando uma pessoa
pessoa = Pessoa("João", 18, 70, 170)

# Apresentando os dados iniciais
print("Dados iniciais:")
pessoa.apresentar()

# Envelhecendo a pessoa em 3 anos
pessoa.envelhecer(3)

# Engordando 5 kg
pessoa.engordar(5)

# Emagrecendo 2 kg
pessoa.emagrecer(2)

# Apresentando os dados atualizados
print("\nDados após envelhecer, engordar e emagrecer:")
pessoa.apresentar()
