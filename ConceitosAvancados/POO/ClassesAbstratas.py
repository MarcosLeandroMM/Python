"""
Classes abstratas em Python são classes que não podem ser instanciadas diretamente, servindo como modelos para outras classes. Elas são parte do módulo abc (Abstract Base Classes) e permitem definir interfaces ou métodos que devem ser implementados por classes derivadas. Vou explicar os conceitos avançados de classes abstratas em Python e fornecer alguns exemplos.

Conceitos Avançados:

Métodos abstratos: Classes abstratas podem conter métodos abstratos, que são definidos usando o decorador @abstractmethod. Esses métodos não têm implementação na classe abstrata e devem ser implementados por qualquer classe derivada.

Classes concretas: Classes derivadas de uma classe abstrata devem fornecer implementações para todos os métodos abstratos da classe base. Caso contrário, elas também serão tratadas como abstratas e não podem ser instanciadas.

Herança múltipla: É possível herdar de múltiplas classes abstratas em uma única classe concreta. No entanto, a classe concreta deve fornecer implementações para todos os métodos abstratos herdados.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# A tentativa de instanciar uma classe abstrata gera um erro:
# shape = Shape()  # Isso resultaria em um erro `TypeError`

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Área do círculo:", circle.area())
print("Área do retângulo:", rectangle.area())

"""Neste exemplo, Shape é uma classe abstrata com um método abstrato area. As classes Circle e Rectangle herdam de Shape e fornecem implementações para o método area. Você não pode instanciar objetos da classe abstrata Shape, mas pode criar objetos de suas classes derivadas. """

class Walk(ABC):
    @abstractmethod
    def walk(self):
        pass

class Swim(ABC):
    @abstractmethod
    def swim(self):
        pass

class Amphibian(Walk, Swim):
    def walk(self):
        print("Walking on land")

    def swim(self):
        print("Swimming in water")

frog = Amphibian()
frog.walk()
frog.swim()

"""Neste exemplo, a classe Amphibian herda de duas classes abstratas, Walk e Swim, e fornece implementações para os métodos walk e swim. Isso demonstra a herança múltipla com classes abstratas."""