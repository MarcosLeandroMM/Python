"""
O tratamento avançado de exceções em Python envolve não apenas capturar exceções, mas também criar exceções personalizadas, usar a cláusula finally e realizar tratamento de exceções assíncrono. Vou explicar esses conceitos avançados e fornecer exemplos para ilustrar cada um deles.

1. Exceções Personalizadas:

Às vezes, é útil criar exceções personalizadas para representar erros específicos do seu aplicativo. Isso pode tornar o código mais legível e permitir um tratamento mais específico de erros.

Exemplo:

"""

class ValorNegativoError(Exception):
    pass

def dividir(a, b):
    if b < 0:
        raise ValorNegativoError("O divisor não pode ser negativo")
    return a / b

try:
    resultado = dividir(10, -2)
except ValorNegativoError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")

"""
Neste exemplo, ValorNegativoError é uma exceção personalizada que é levantada se um divisor for negativo.
"""

"""Cláusula finally:

A cláusula finally é usada para definir código que sempre será executado, independentemente de ocorrer uma exceção ou não. Isso é útil para ações de limpeza, como fechar arquivos ou conexões de banco de dados, que devem ser executadas independentemente do resultado da exceção.

Exemplo:
"""
try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado")
else:
    print("Conteúdo do arquivo:", conteudo)
finally:
    arquivo.close()  # Isso será executado sempre

"""
 Tratamento de Exceções Assíncrono:

Em Python 3.5 e posteriores, você pode usar asyncio para tratar exceções em código assíncrono. O tratamento de exceções em código assíncrono é semelhante ao tratamento de exceções em código síncrono, mas envolve o uso de await e try/except em operações assíncronas.

Exemplo:
"""

import asyncio

async def funcao_assincrona():
    try:
        resultado = await operacao_assincrona()
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {resultado}")

async def operacao_assincrona():
    await asyncio.sleep(2)
    raise ValueError("Erro na operação assíncrona")

loop = asyncio.get_event_loop()
loop.run_until_complete(funcao_assincrona())

"""
Neste exemplo, asyncio é usado para lidar com operações assíncronas, e a cláusula try/except é usada para capturar exceções em código assíncrono.

O tratamento avançado de exceções em Python é importante para lidar com situações mais complexas e garantir que seu código seja robusto e seguro. Você pode criar exceções personalizadas para representar erros específicos de seu aplicativo, usar a cláusula finally para ações de limpeza e aplicar o tratamento de exceções em código assíncrono usando asyncio. Isso torna seu código mais eficiente e seguro.

"""