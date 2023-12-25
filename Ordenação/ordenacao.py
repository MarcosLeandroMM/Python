"""
As listas em Python possuem um método embutido list.sort() que modifica a lista em si. Há também a função embutida sorted() que constrói uma nova lista ordenada à partir de um iterável.

Neste documento, exploramos várias técnicas para ordenar dados utilizando Python.

Básico de Ordenação
Uma ordenação ascendente simples é muito fácil: apenas chame a função sorted(). Retorna uma nova lista ordenada:
"""
sorted([5,2,3,1,4])

"""
Você também pode utilizar o método list.sort(). Isso modifica a lista em si (e retorna None para evitar confusão). Usualmente este método é menos conveniente que a função sorted() - mas se você não precisará da lista original, esta maneira é levemente mais eficiente.
"""
a = [5,2,3,1,4]
a.sort()

"""
Outra diferença é que o método list.sort() é aplicável apenas às listas. Em contrapartida, a função sorted() aceita qualquer iterável.
"""
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})

"""
Tanto o método list.sort() quanto a função sorted() possuem um parâmetro key que especifica uma função (ou outro chamável) a ser chamada para cada elemento da lista antes de ser realizada a comparação.

Por exemplo, aqui há uma comparação case-insensitive de strings
"""

sorted("This is a test string from Andrew".split(), key=str.lower)

"""O valor do parâmetro key deve ser uma função (ou outro chamável) que recebe um único argumento e retorna uma chave à ser utilizada com o propósito de ordenação. Esta técnica é rápida porque a função chave é chamada exatamente uma vez para cada entrada de registro.

Uma padrão comum é ordenar objetos complexos utilizando algum índice do objeto como chave. Por exemplo:
"""

student_tuples = [
    ('jhon', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
# isso fará uma ordenação por idade

# a mesma técnica funciona com objetos que possuem atributos nomeados. Por exemplo:
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
student_objects = [
    Student('jhon', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)

"""Funções do Módulo Operator
O padrão de chave-função mostrado acima é muito comum, por isso, Python provê funções convenientes para tornar as funções de acesso mais fáceis e rápidas. O módulo operator tem as funções itemgetter(), attrgetter(), e methodcaller()

Usando estas funções, os exemplos acima se tornam mais simples e mais rápidos:
"""
from operator import itemgetter, attrgetter

# ordenando por idade
sorted(student_tuples, key=itemgetter(2))

# odenando por grade e depois por idade
