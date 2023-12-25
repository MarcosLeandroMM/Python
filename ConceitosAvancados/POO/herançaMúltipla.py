"""A herança múltipla em Python é um recurso avançado que permite que uma classe herde atributos e métodos de várias classes base. Isso significa que uma classe pode ter várias classes base, o que pode ser útil para criar classes mais flexíveis e reutilizáveis. No entanto, a herança múltipla pode ser complexa e requer cuidado para evitar conflitos de nomes e problemas de design. Vou explicar os conceitos avançados da herança múltipla em Python e fornecer alguns exemplos.

Conceitos Avançados:

Ordem de Resolução de Métodos (MRO): Em herança múltipla, a ordem em que as classes base são declaradas importa. O Python usa o algoritmo C3 para determinar a ordem de resolução de métodos (MRO), que define a prioridade na busca de métodos em classes base. Você pode visualizar a MRO de uma classe usando Classe.mro().

Conflitos de Nomes: Quando duas classes base têm métodos ou atributos com o mesmo nome, pode ocorrer um conflito. Você deve definir qual método ou atributo deseja usar na classe derivada.

Uso de super(): O uso de super() permite chamar um método na classe base da MRO atual. Isso é útil para evitar chamadas diretas a métodos da classe base e manter o código flexível. """

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    def show(self):
        super().show()  # Chama o método da classe base na MRO atual
        print("D")

d = D()
d.show()

"""
Neste exemplo, a classe D herda de B e C, que ambas herdam de A. A ordem de resolução de métodos é D -> B -> C -> A. O método show de D chama super().show(), que chama o método de B, seguido por seu próprio "D".
"""

class Engine:
    def start(self):
        print("Engine started")

class ElectricMotor:
    def start(self):
        print("Electric motor started")

class HybridCar(Engine, ElectricMotor):
    pass

car = HybridCar()
car.start()  # Qual método `start` deve ser chamado?
"""Neste exemplo, a classe HybridCar herda de Engine e ElectricMotor, ambas das quais têm um método start. O método start de ElectricMotor é chamado, pois aparece antes na ordem de resolução de métodos. """
