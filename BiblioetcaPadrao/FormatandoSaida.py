'''
Formatando a saída
O módulo reprlib fornece uma versão de repr() personalizado para exibições abreviadas de contêineres grandes ou profundamente aninhados:
'''

import reprlib 
reprlib.repr(set('supercalifragilisticexpialidocious'))
