'''Corrotinas em Python: Uma Visão Detalhada

Introdução:

Corrotinas são uma característica poderosa em Python que permitem a execução assíncrona de código. Introduzidas pela PEP 492 em Python 3.5, as corrotinas oferecem uma maneira eficiente de lidar com operações assíncronas, como entrada/saída (E/S), sem o uso explícito de threads ou processos.

Principais Conceitos:

async def e await: Corrotinas são definidas usando a sintaxe async def, e a palavra-chave await é usada dentro delas para suspender a execução até que a operação assíncrona seja concluída. '''

import asyncio 

async def minha_corrotina():
    print("Início da corrotina")
    await asyncio.sleep(1)
    print("Fim da corrotina")

'''
Objetivo Principal: O principal objetivo das corrotinas é permitir que operações assíncronas ocorram sem bloquear a execução de outros trechos de código. Isso é especialmente útil em situações onde a espera por E/S pode ser otimizada sem a necessidade de criar threads ou processos adicionais.

Funcionamento Interno:

Sintaxe e Semântica:

Corrotinas são definidas usando async def e chamadas usando await.
Elas podem ser suspensas e retomadas, permitindo que outras corrotinas sejam executadas enquanto uma espera por uma operação assíncrona.
As corrotinas retornam objetos chamados "coro-objetos", que podem ser usados para controlar a execução e obter resultados.
asyncio: O módulo asyncio é fundamental para o funcionamento eficiente das corrotinas. Ele fornece um loop de eventos que gerencia a execução assíncrona e a coordenação entre diferentes corrotinas.

'''

import asyncio

async def main():
    await asyncio.gather(corrotina1(), corrotina2())

asyncio.run(main())


# Operações Assíncronas Simples:

import asyncio

async def minha_corrotina():
    print("Início da corrotina")
    await asyncio.sleep(1)
    print("Fim da corrotina")

asyncio.run(minha_corrotina())


# Execução Concorrente:

import asyncio

async def corrotina1():
    print("Corrotina 1 iniciada")
    await asyncio.sleep(2)
    print("Corrotina 1 concluída")

async def corrotina2():
    print("Corrotina 2 iniciada")
    await asyncio.sleep(1)
    print("Corrotina 2 concluída")

async def main():
    await asyncio.gather(corrotina1(), corrotina2())

asyncio.run(main())


# Tratamento de Múltiplos Resultados:

import asyncio

async def corrotina1():
    await asyncio.sleep(2)
    return "Resultado da Corrotina 1"

async def corrotina2():
    await asyncio.sleep(1)
    return "Resultado da Corrotina 2"

async def main():
    resultado1, resultado2 = await asyncio.gather(corrotina1(), corrotina2())
    print(resultado1, resultado2)

asyncio.run(main())

'''
Considerações Finais:

Limitações: Corrotinas são mais adequadas para operações E/S assíncronas e não são recomendadas para tarefas intensivas em CPU. Para essas tarefas, outras abordagens, como threads ou processos, podem ser mais apropriadas.

Concorrência vs. Paralelismo: Corrotinas oferecem concorrência, mas não paralelismo real, pois uma única thread é usada para executar todas as corrotinas. No entanto, a concorrência é eficaz para evitar bloqueios em operações de E/S.

asyncio vs. threading/multiprocessing: A escolha entre corrotinas e outras formas de concorrência depende das características específicas do problema. Corrotinas são uma ferramenta poderosa, especialmente quando lidamos com E/S assíncrona.

Comunicação Entre Corrotinas: Para comunicação entre corrotinas, pode-se usar objetos como asyncio.Queue ou asyncio.Event para coordenar a execução.

As corrotinas em Python são uma parte essencial da programação assíncrona e oferecem uma maneira eficiente e elegante de lidar com tarefas concorrentes, especialmente aquelas relacionadas a operações de E/S.


'''