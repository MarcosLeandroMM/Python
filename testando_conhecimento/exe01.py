# Crie uma classe Student com os atributos name, age, e grades (uma lista de notas). Implemente um método para calcular a média das notas do aluno.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calc_notas(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

aluno = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
notas = input("Digite as notas do aluno separadas por vírgula: ")
notas = [float(nota) for nota in notas.split(",")]


student1 = Student(aluno, idade, notas)


media = student1.calc_notas()


print(f" O aluno {aluno} com idade {idade} teve média de {media} ")

        
