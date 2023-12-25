'''
Python inclui diversas estruturas de dados compostas, usadas para agrupar outros valores. A mais versátil é list (lista), que pode ser escrita como uma lista de valores (itens) separados por vírgula, entre colchetes. Os valores contidos na lista não precisam ser todos do mesmo tipo.

'''

squares = [1,4,9,16,25]

# Como strings (e todos os tipos embutidos de sequência), listas pode ser indexados e fatiados:
squares[0]  # indexing returns the item
1
squares[-1]
25
squares[-3:]  # slicing returns a new list
[9, 16, 25]

# As listas também suportam operações como concatenação:
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Diferentemente de strings, que são imutáveis, listas são mutáveis, ou seja, é possível alterar elementos individuais de uma lista:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
64
cubes[3] = 64  # replace the wrong value
cubes
[1, 8, 27, 64, 125]

# Você também pode adicionar novos itens no final da lista, usando o método append() (estudaremos mais a respeito dos métodos posteriormente):
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
[1, 8, 27, 64, 125, 216, 343]

# Atribuição a fatias também é possível, e isso pode até alterar o tamanho da lista ou remover todos os itens dela:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
[]

# É possível aninhar listas (criar listas contendo outras listas), por exemplo:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]

# O argumento end pode ser usado para evitar uma nova linha após a saída ou finalizar a saída com uma string diferente:
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,














'''
As listas são sequências mutáveis, normalmente usadas para armazenar coleções de itens homogêneos (onde o grau preciso de similaridade variará de acordo com a aplicação).

class list([iterable])
As listas podem ser construídas de várias maneiras:

Usando um par de colchetes para denotar uma lista vazia: []

Usando colchetes, separando itens por vírgulas: [a], [a, b, c]

Usando uma compreensão de lista: [x for x in iterable]

Usando o construtor de tipo: list() ou list(iterable)

O construtor produz uma lista cujos itens são iguais e na mesma ordem que os itens de iterable. iterable pode ser uma sequência, um contêiner que suporte iteração ou um objeto iterador. Se iterable já for uma lista, uma cópia será feita e retornada, semelhante a iterable[:]. Por exemplo, list('abc') retorna ['a', 'b', 'c'] e list( (1, 2, 3) ) retorna [1, 2, 3]. Se nenhum argumento for dado, o construtor criará uma nova lista vazia [].

Muitas outras operações também produzem listas, incluindo a função embutida sorted().

Listas implementam todas as operações de sequências comuns e mutáveis. As listas também fornecem o seguinte método adicional:

sort(*, key=None, reverse=False)
Esse método classifica a lista in-place, usando apenas comparações < entre itens. As exceções não são suprimidas – se qualquer operação de comparação falhar, toda a operação de ordenação falhará (e a lista provavelmente será deixada em um estado parcialmente modificado).

sort() aceita 2 argumentos que só podem ser passados como argumentos somente-nomeados:

key especifica uma função de um argumento que é usado para extrair uma chave de comparação de cada elemento da lista (por exemplo, key=str.lower). A chave correspondente a cada item na lista é calculada uma vez e depois usada para todo o processo de classificação. O valor padrão None significa que os itens da lista são classificados diretamente sem calcular um valor de chave separado.

A função utilitária functools.cmp_to_key() está disponível para converter a função cmp no estilo 2.x para uma função key.

reverse é um valor booleano. Se definido igual a True, então os elementos da lista são classificados como se cada comparação estivesse invertida.

Este método modifica a sequência in-place para economizar espaço ao classificar uma sequência grande. Para lembrar aos usuários que os mesmos operam por efeito colateral, ele não retorna a sequência ordenada (utilize a função sorted() para solicitar explicitamente uma nova instância da lista ordenada).

O método sort() é garantido como sendo estável. Uma classificação é estável se ela garantir não alterar a ordem relativa de elementos que comparam igual – isso é útil para classificar em várias passagens (por exemplo, classificar por departamento, depois por nota salarial).

Para exemplos de classificação e um breve tutorial de classificação, veja HowTo - Ordenação.

Detalhes da implementação do CPython: No momento em que uma lista está sendo ordenada, o efeito de tentar alterar, ou mesmo inspecionar, a lista é indefinida. A implementação C do Python faz com que a lista apareça vazia durante o tempo de processamento, e levanta a exceção ValueError se puder detectar que a lista foi alterada durante uma ordenação.

As listas em Python possuem um método embutido list.sort() que modifica a lista em si. Há também a função embutida sorted() que constrói uma nova lista ordenada à partir de um iterável.

Neste documento, exploramos várias técnicas para ordenar dados utilizando Python.

Básico de Ordenação
Uma ordenação ascendente simples é muito fácil: apenas chame a função sorted(). Retorna uma nova lista ordenada:

'''

sorted([5, 2, 3, 1, 4 ])
# [1, 2, 3, 4, 5]

'''
Você também pode utilizar o método list.sort(). Isso modifica a lista em si (e retorna None para evitar confusão). Usualmente este método é menos conveniente que a função sorted() - mas se você não precisará da lista original, esta maneira é levemente mais eficiente.
'''
a = [5,2,3,1,4]
a.sort()

# Outra diferença é que o método list.sort() é aplicável apenas às listas. Em contrapartida, a função sorted() aceita qualquer iterável.

# Funções Chave
'''
Tanto o método list.sort() quanto a função sorted() possuem um parâmetro key que especifica uma função (ou outro chamável) a ser chamada para cada elemento da lista antes de ser realizada a comparação.

Por exemplo, aqui há uma comparação case-insensitive de strings.
'''
sorted("This is a test string from Marcos". slipt(), key=str.lower())

'''O valor do parâmetro key deve ser uma função (ou outro chamável) que recebe um único argumento e retorna uma chave à ser utilizada com o propósito de ordenação. Esta técnica é rápida porque a função chave é chamada exatamente uma vez para cada entrada de registro.'''

# Uma padrão comum é ordenar objetos complexos utilizando algum índice do objeto como chave. Por exemplo:

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2]) # sorted by age

# A mesma técnica funciona com objetos que possuem atributos nomeados. Por exemplo:

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)
# sorted by age

'''Funções do Módulo Operator
O padrão de chave-função mostrado acima é muito comum, por isso, Python provê funções convenientes para tornar as funções de acesso mais fáceis e rápidas. O módulo operator tem as funções itemgetter(), attrgetter(), e methodcaller()

Usando estas funções, os exemplos acima se tornam mais simples e mais rápidos

'''

from operator import itemgeetter, attrgetter

sorted(student_tuples, key=itemgeetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# As funções do módulo operator permite múltiplos níveis de ordenação. Por exemplo, ordenar por grade e então por age:
sorted(student_tuples, key=itemgeetter(1,2))
# [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

'''
Ascendente e Descendente
Tanto o método list.sort() quanto a função sorted() aceitam um valor booleano para o parâmetro reverse. Essa flag é utilizada para ordenações descendentes. Por exemplo, para retornar os dados de estudantes pela ordem inversa de age:
'''
sorted(student_tuples, key=itemgeetter(2), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(student_objects, key=attrgetter('age'), reverse=True)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

''' Estabilidade de Ordenação e Ordenações Complexas
Ordenações são garantidas de serem estáveis. Isso significa que quando múltiplos registros possuem a mesma chave, eles terão sua ordem original preservada.
'''
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgeetter(0))
# [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]


