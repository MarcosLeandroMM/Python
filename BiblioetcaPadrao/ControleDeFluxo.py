'''
Comandos if
Provavelmente o mais conhecido comando de controle de fluxo é o if. Por exemplo:

'''

x = int(input("Please enter an integer: "))
# Please enter an integer: 42

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

'''
Pode haver zero ou mais partes elif, e a parte else é opcional. A palavra-chave ‘elif’ é uma abreviação para ‘else if’, e é útil para evitar indentação excessiva. Uma sequência if … elif … elif … substitui os comandos switch ou case, encontrados em outras linguagens.

Se você está comparando o mesmo valor com várias constantes, ou verificando por tipos ou atributos específicos, você também pode achar a instrução match útil. Para mais detalhes veja Instruções match.

'''

'''Comandos for
O comando for em Python é um pouco diferente do que costuma ser em C ou Pascal. Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal), ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), o comando for do Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. Por exemplo:'''

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# cat 3
# window 6
# defenestrate 12

# Código que modifica uma coleção sobre a qual está iterando pode ser inseguro. No lugar disso, usualmente você deve iterar sobre uma cópia da coleção ou criar uma nova coleção:

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', 'Marcos': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy.items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

'''
 A função range()¶
Se você precisa iterar sobre sequências numéricas, a função embutida range() é a resposta. Ela gera progressões aritméticas:

'''
for i in range(5):
    print(i)

# 0,1,2,3,4,5,

'''
O ponto de parada fornecido nunca é incluído na lista; range(10) gera uma lista com 10 valores, exatamente os índices válidos para uma sequência de comprimento 10. É possível iniciar o intervalo com outro número, ou alterar a razão da progressão (inclusive com passo negativo):

'''

list(range(5,10))
[5,6,7,8,9]

list(range(0,10,3)) # início: 0, tamanho-lista: 10, intervalo: 3
[0,3,6,9]

list(range(-10, -100, -30))
[-10, -40, -70]


# Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:
a = ['Mary', 'had', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])