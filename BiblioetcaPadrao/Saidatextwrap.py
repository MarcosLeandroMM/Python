# O módulo textwrap formata parágrafos de texto para que caibam em uma dada largura de tela:

import textwrap 

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))