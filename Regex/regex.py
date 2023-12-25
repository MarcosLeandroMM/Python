"""

Expressões Regulares (Regex) em Python

As expressões regulares, ou Regex, são sequências de caracteres que formam padrões de pesquisa. Elas são utilizadas para buscar, corresponder e manipular strings de texto de maneira eficiente. Em Python, o módulo re fornece funcionalidades para trabalhar com expressões regulares.

Aqui estão alguns conceitos fundamentais em expressões regulares:

Meta-caracteres:

São caracteres com significados especiais. Alguns exemplos incluem:
.: Corresponde a qualquer caractere, exceto uma nova linha.
^: Corresponde ao início da string.
$: Corresponde ao final da string.
Quantificadores:

São usados para especificar a quantidade de ocorrências de um caractere ou grupo.
*: Corresponde a 0 ou mais ocorrências.
+: Corresponde a 1 ou mais ocorrências.
?: Corresponde a 0 ou 1 ocorrência.
{n}: Corresponde exatamente a n ocorrências.
{n,}: Corresponde a n ou mais ocorrências.
{n,m}: Corresponde a pelo menos n e no máximo m ocorrências.
Grupos de Captura:

São usados para agrupar parte de um padrão. O que é correspondido por um grupo pode ser recuperado separadamente.
( e ): Define um grupo de captura.
Classes de Caracteres:

São usadas para especificar um conjunto de caracteres que você deseja corresponder.
[...]: Corresponde a qualquer caractere dentro dos colchetes.
[^...]: Corresponde a qualquer caractere que não esteja dentro dos colchetes.
Âncoras:

São usadas para especificar a posição em que a correspondência deve ocorrer na string.
\b: Corresponde a uma posição de fronteira de palavra.
\B: Corresponde a uma posição que não é uma fronteira de palavra.


"""


import re

# Padroniza um número de telefone no formato (ddd) ddd-dddd
padrao_telefone = re.compile(r'\(\d{3}\) \d{3}-\d{4}')

# Texto de exemplo
texto = "Entre em contato no telefone (123) 456-7890."

# Procura por padrões de telefone no texto
correspondencias = padrao_telefone.search(texto)

# Imprime as correspondências encontradas
if correspondencias:
    print("Número de telefone encontrado:", correspondencias.group())
else:
    print("Nenhum número de telefone encontrado.")
