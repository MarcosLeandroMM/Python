'''
O módulo locale acessa uma base de dados de formatos específicos a determinada cultura. O atributo de agrupamento da função “format” oferece uma forma direta de formatar números com separadores de grupo:
'''

import locale

locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
x = 1234567.8
locale.format_string("%d", x, grouping=True)
locale.format_string("%s%,*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)