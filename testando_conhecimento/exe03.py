# Crie uma classe Car com os atributos marca, modelo, e ano. Implemente um método para imprimir as informações do carro em um formato legível.

class Car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        return f"A marca: {self.marca}, modelo:{self.modelo}, ano: {self.ano}"

carro = Car("Mercedes", "BMW", 2018)

info_car = carro.mostrar_info()

print(f"O carro tem as seguintes informações {info_car}")