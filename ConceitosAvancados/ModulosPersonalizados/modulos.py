"""Módulos e pacotes personalizados são conceitos fundamentais em Python que permitem a organização e reutilização de código. Eles são usados para dividir seu código em componentes mais gerenciáveis, criar abstrações e facilitar a colaboração com outros desenvolvedores. Vou explicar esses conceitos em detalhes e fornecer exemplos para ilustrar como criar módulos e pacotes personalizados.

Módulos Personalizados:

Um módulo é um arquivo Python que contém variáveis, funções e classes relacionadas. Você pode criar seus próprios módulos para encapsular funcionalidades específicas e reutilizáveis. Para criar um módulo personalizado, siga estes passos:

Crie um arquivo Python com extensão .py, por exemplo, meu_modulo.py.
Defina variáveis, funções ou classes no arquivo.
Para usá-lo em outro arquivo, importe o módulo usando a instrução import.
Exemplo de um módulo personalizado (meu_modulo.py):"""


meu_modulo.py

def saudacao(nome):
    return f"Olá, {nome}!"

numero = 42

#Exemplo de uso em outro arquivo:


# outro_arquivo.py

import meu_modulo

print(meu_modulo.saudacao("Alice"))  # Saída: Olá, Alice!
print(meu_modulo.numero)  # Saída: 42
"""Pacotes Personalizados:

Um pacote é um diretório que contém módulos relacionados e um arquivo especial __init__.py. Os pacotes permitem que você organize seus módulos em uma hierarquia de diretórios. Para criar um pacote personalizado, siga estes passos:

Crie um diretório com um nome significativo.
Dentro do diretório, coloque módulos Python (arquivos .py) que deseja incluir no pacote.
Crie um arquivo vazio chamado __init__.py no diretório para indicar que ele é um pacote.
Estrutura de um pacote personalizado:"""


meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py

# Exemplo de uso de pacotes:


# Importando um módulo de um pacote personalizado
from meu_pacote import modulo1

print(modulo1.funcao_do_modulo1())

"""Vantagens de Módulos e Pacotes Personalizados:

Organização: Dividir seu código em módulos e pacotes facilita a organização e manutenção.
Reutilização: Você pode reutilizar módulos e pacotes em vários projetos.
Colaboração: Módulos e pacotes bem organizados facilitam a colaboração com outros desenvolvedores, pois o código fica mais modular e compreensível.
Abstração: Você pode criar abstrações em seus módulos, tornando seu código mais legível e reutilizável.
A criação de módulos e pacotes personalizados é uma prática comum e recomendada em Python para projetos maiores e mais complexos. Isso ajuda a manter seu código organizado, facilita a manutenção e promove a reutilização de código, tornando-o mais eficiente e escalável."""