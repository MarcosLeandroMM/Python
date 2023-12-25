"""
A mais útil das três é especificar um valor padrão para um ou mais argumentos. Isso cria uma função que pode ser invocada com menos argumentos do que os que foram definidos. Por exemplo:
"""

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

"""
Essa função pode ser chamada de várias formas:

fornecendo apenas o argumento obrigatório: ask_ok('Do you really want to quit?')

fornecendo um dos argumentos opcionais: ask_ok('OK to overwrite the file?', 2)

ou fornecendo todos os argumentos: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

""" 