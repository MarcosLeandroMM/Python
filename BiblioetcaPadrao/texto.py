'''
3.1.2. Texto
Python pode manipular texto (representado pelo tipo str, também chamado de “strings”), bem como números. Isso inclui caracteres “!”, palavras “coelho”, nomes “Paris”, frases “Eu te protejo.”, etc. “Oba! :)”. Eles podem ser colocados entre aspas simples ('...') ou aspas duplas ("...") com o mesmo resultado 2.
'''

# Para colocar aspas entre aspas, precisamos “escapá-la”, precedendo-as com \. Alternativamente, podemos usar o outro tipo de aspas:
print('doesn\'t')

'''
Se não quiseres que os caracteres sejam precedidos por \ para serem interpretados como caracteres especiais, poderás usar strings raw (N.d.T: “crua” ou sem processamento de caracteres de escape) adicionando um r antes da primeira aspa:

print('C:\some\name')  # here \n means newline!
C:\some
ame
print(r'C:\some\name')  # note the r before the quote
C:\some\name

Há um aspecto sutil nas strings raw: uma string raw não pode terminar em um número ímpar de caracteres \; consulte a entrada do FAQ para mais informações e soluções alternativas.

'''


# As strings literais podem abranger várias linhas. 
# Uma maneira é usar as aspas triplas: """...""" ou ''' ...'''. 
# O fim das linhas é incluído automaticamente na string, mas é possível evitar isso adicionando uma \ no final. O seguinte exemplo

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

'''
As strings podem ser indexadas (subscritas), com o primeiro caractere como índice 0. Não existe um tipo específico para caracteres; um caractere é simplesmente uma string cujo tamanho é 1:

'''
# As strings podem ser indexadas (subscritas), com o primeiro caractere como índice 0. Não existe um tipo específico para caracteres; um caractere é simplesmente uma string cujo tamanho é 1
word = 'Python'
print(word[2])

# Índices também podem ser números negativos para iniciar a contagem pela direita:
print(word[-2])

# Além da indexação, o fatiamento também é permitido. Embora a indexação seja usada para obter caracteres individuais, fatiar permite que você obtenha uma substring:

word[:2]   # character from the beginning to position 2 (excluded)
'Py'
word[4:]   # characters from position 4 (included) to the end
'on'
word[-2:]  # characters from the second-last (included) to the end
'on'

# Observe como o início sempre está incluído, e o fim sempre é excluído. Isso garante que s[:i] + s[i:] seja sempre igual a s:
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'

# As strings do Python não podem ser alteradas — uma string é imutável. Portanto, atribuir a uma posição indexada na sequência resulta em um erro


# Se você precisar de uma string diferente, deverá criar uma nova:
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'